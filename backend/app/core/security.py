from datetime import UTC, datetime, timedelta

from fastapi import HTTPException, Response, status
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

AUTH_COOKIE_NAME = "access_token"
COOKIE_PATH = "/api"
COOKIE_SAMESITE = "none"  # Required for cross-site (Vercel + Fly.io)
COOKIE_SECURE = True  # Required with SameSite=None


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(
    data: dict, expires_delta: timedelta | None = None, is_admin: bool = False
) -> tuple[str, str]:
    """Create JWT access token and return (token, csrf_token)"""
    import secrets

    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        hours = (
            settings.ADMIN_TOKEN_EXPIRE_HOURS
            if is_admin
            else settings.ACCESS_TOKEN_EXPIRE_HOURS
        )
        expire = datetime.now(UTC) + timedelta(hours=hours)

    csrf_token = secrets.token_urlsafe(32) if settings.ENABLE_CSRF else ""

    to_encode.update(
        {
            "exp": expire,
            "is_admin": is_admin,
            "aud": "echostor-security-tool",
            "iss": "echostor-api",
            "iat": datetime.now(UTC),
            "csrf": csrf_token,
        }
    )
    encoded_jwt = jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )
    return encoded_jwt, csrf_token


def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM],
            audience="echostor-security-tool",
            issuer="echostor-api",
        )
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


def set_auth_cookie(response: Response, token: str, max_age: int) -> None:
    """Set authentication cookie with consistent security attributes"""
    response.set_cookie(
        key=AUTH_COOKIE_NAME,
        value=token,
        max_age=max_age,
        path=COOKIE_PATH,
        httponly=True,
        secure=COOKIE_SECURE,
        samesite=COOKIE_SAMESITE,
    )


def clear_auth_cookie(response: Response) -> None:
    """Clear authentication cookie with same attributes used to set it"""
    response.set_cookie(
        key=AUTH_COOKIE_NAME,
        value="",
        max_age=0,
        path=COOKIE_PATH,
        httponly=True,
        secure=COOKIE_SECURE,
        samesite=COOKIE_SAMESITE,
    )


def generate_admin_password() -> tuple[str, str]:
    """Generate a secure admin password and return both plain and hashed versions"""
    import secrets
    import string

    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(secrets.choice(alphabet) for _ in range(16))
    hashed = get_password_hash(password)

    return password, hashed
