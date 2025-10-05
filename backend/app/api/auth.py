from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.core.database import get_write_db, get_read_db
from app.core.security import verify_password, get_password_hash, create_access_token, verify_token
from app.core.config import settings
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin, Token, UserResponse

router = APIRouter()
security = HTTPBearer()

@router.post("/register", response_model=Token)
async def register(user_data: UserCreate, db: Session = Depends(get_write_db)):
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    hashed_password = get_password_hash(user_data.password)
    db_user = User(
        email=user_data.email,
        full_name=user_data.full_name,
        company_name=user_data.company_name,
        password_hash=hashed_password
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    access_token = create_access_token(
        data={
            "sub": db_user.email, 
            "user_id": str(db_user.id), 
            "is_admin": db_user.is_admin if hasattr(db_user, 'is_admin') else False
        }
    )
    
    return Token(
        access_token=access_token,
        expires_in=settings.ACCESS_TOKEN_EXPIRE_HOURS * 3600,
        user=UserResponse.model_validate(db_user)
    )

@router.post("/login", response_model=Token)
async def login(user_credentials: UserLogin, db: Session = Depends(get_read_db)):
    if (settings.ADMIN_LOGIN_USER and 
        user_credentials.email == settings.ADMIN_LOGIN_USER and
        settings.ADMIN_LOGIN_PASSWORD):
        
        if user_credentials.password == settings.ADMIN_LOGIN_PASSWORD:
            access_token = create_access_token(
                data={"sub": settings.ADMIN_LOGIN_USER, "is_admin": True},
                is_admin=True
            )
            
            return Token(
                access_token=access_token,
                expires_in=settings.ADMIN_TOKEN_EXPIRE_HOURS * 3600
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password"
            )
    
    if user_credentials.email == settings.ADMIN_EMAIL:
        if not settings.ADMIN_PASSWORD_HASH:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Admin password not configured"
            )
        
        if not verify_password(user_credentials.password, settings.ADMIN_PASSWORD_HASH):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password"
            )
        
        access_token = create_access_token(
            data={"sub": settings.ADMIN_EMAIL, "is_admin": True},
            is_admin=True
        )
        
        return Token(
            access_token=access_token,
            expires_in=settings.ADMIN_TOKEN_EXPIRE_HOURS * 3600
        )
    
    
    user = db.query(User).filter(User.email == user_credentials.email).first()
    if not user or not verify_password(user_credentials.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    
    access_token = create_access_token(
        data={
            "sub": user.email, 
            "user_id": str(user.id), 
            "is_admin": user.is_admin if hasattr(user, 'is_admin') else False
        }
    )
    
    return Token(
        access_token=access_token,
        expires_in=settings.ACCESS_TOKEN_EXPIRE_HOURS * 3600,
        user=UserResponse.model_validate(user)
    )

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_write_db)
):
    token_data = verify_token(credentials.credentials)
    
    if token_data.get("is_admin") and token_data.get("user_id"):
        user_id = token_data.get("user_id")
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            return user
    
    if token_data.get("is_admin"):
        admin_email = settings.ADMIN_LOGIN_USER if settings.ADMIN_LOGIN_USER else settings.ADMIN_EMAIL
        return {"email": admin_email, "is_admin": True}
    
    email = token_data.get("sub")
    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )
    
    
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    return user

async def get_current_admin_user(current_user = Depends(get_current_user)):
    if hasattr(current_user, 'is_admin') and current_user.is_admin:
        return {"email": current_user.email, "is_admin": True, "user_id": str(current_user.id)}
    elif isinstance(current_user, dict) and current_user.get("is_admin"):
        return current_user
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )

@router.get("/me", response_model=UserResponse)
async def get_current_user_info(current_user = Depends(get_current_user)):
    if isinstance(current_user, dict) and current_user.get("is_admin"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Admin user info not available"
        )
    return UserResponse.model_validate(current_user)
