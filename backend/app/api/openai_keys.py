"""Admin API endpoints for OpenAI API key management."""

import os

from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

from app.api.auth import get_current_admin_user
from app.core.config import settings
from app.core.database import get_db
from app.schemas.openai_key import (
    OpenAIKeyCreate,
    OpenAIKeyResponse,
    OpenAIKeyTest,
    OpenAIKeyTestResponse,
    OpenAIKeyToggle,
)
from app.schemas.user import CurrentUserResponse
from app.services.openai_key_manager import OpenAIKeyManager
from app.utils.encryption import get_encryption_key

router = APIRouter()


@router.get("/", response_model=list[OpenAIKeyResponse])
async def list_openai_keys(
    request: Request,
    include_inactive: bool = False,
    current_admin: CurrentUserResponse = Depends(get_current_admin_user),
    db: Session = Depends(get_db),
):
    """List all OpenAI API keys with masked values."""
    try:
        with OpenAIKeyManager(db) as manager:
            keys = manager.list_keys(include_inactive=include_inactive)
            return keys
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to list API keys: {str(e)}",
        )


@router.post("/", response_model=OpenAIKeyResponse)
async def create_openai_key(
    request: Request,
    key_data: OpenAIKeyCreate,
    current_admin: CurrentUserResponse = Depends(get_current_admin_user),
    db: Session = Depends(get_db),
):
    """Add a new OpenAI API key."""
    try:
        with OpenAIKeyManager(db) as manager:
            key = manager.add_key(
                key_name=key_data.key_name,
                api_key=key_data.api_key,
                created_by=current_admin.email,
            )

            keys = manager.list_keys(include_inactive=True)
            for k in keys:
                if k["id"] == key.id:
                    return k

            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to retrieve created key",
            )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create API key: {str(e)}",
        )


@router.post("/test", response_model=OpenAIKeyTestResponse)
async def test_openai_key(
    request: Request,
    key_data: OpenAIKeyTest,
    current_admin: CurrentUserResponse = Depends(get_current_admin_user),
    db: Session = Depends(get_db),
):
    """Test if an OpenAI API key is valid."""
    try:
        with OpenAIKeyManager(db) as manager:
            is_valid, message = manager.test_key(key_data.api_key)
            return OpenAIKeyTestResponse(is_valid=is_valid, message=message)
    except Exception as e:
        return OpenAIKeyTestResponse(is_valid=False, message=f"Test failed: {str(e)}")


@router.patch("/{key_id}/toggle", response_model=OpenAIKeyResponse)
async def toggle_openai_key(
    request: Request,
    key_id: str,
    toggle_data: OpenAIKeyToggle,
    current_admin: CurrentUserResponse = Depends(get_current_admin_user),
    db: Session = Depends(get_db),
):
    """Toggle an OpenAI API key's active status."""
    try:
        with OpenAIKeyManager(db) as manager:
            manager.toggle_key(key_id, toggle_data.is_active)

            keys = manager.list_keys(include_inactive=True)
            for k in keys:
                if k["id"] == key_id:
                    return k

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Key not found after toggle",
            )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to toggle API key: {str(e)}",
        )


@router.delete("/{key_id}")
async def delete_openai_key(
    request: Request,
    key_id: str,
    current_admin: CurrentUserResponse = Depends(get_current_admin_user),
    db: Session = Depends(get_db),
):
    """Delete an OpenAI API key."""
    try:
        with OpenAIKeyManager(db) as manager:
            manager.delete_key(key_id)
            return {"message": "API key deleted successfully"}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to delete API key: {str(e)}",
        )


@router.get("/diagnostics")
async def encryption_diagnostics(
    request: Request,
    current_admin: CurrentUserResponse = Depends(get_current_admin_user),
):
    """Diagnostic endpoint to check encryption key sources (admin only)."""
    diagnostics = {
        "settings_present": bool(settings.OPENAI_KEYS_ENCRYPTION_KEY),
        "env_present": bool(os.getenv("OPENAI_KEYS_ENCRYPTION_KEY")),
        "secrets_file_exists": os.path.exists("/run/secrets/OPENAI_KEYS_ENCRYPTION_KEY"),
    }
    
    try:
        key = get_encryption_key()
        diagnostics["effective_key_len"] = len(key)
        diagnostics["can_load_key"] = True
    except Exception as e:
        diagnostics["effective_key_len"] = 0
        diagnostics["can_load_key"] = False
        diagnostics["error"] = str(e)
    
    return diagnostics
