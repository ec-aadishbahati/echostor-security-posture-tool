"""Encryption utilities for sensitive data like API keys."""

import logging

from cryptography.fernet import Fernet

from app.core.config import settings

logger = logging.getLogger(__name__)


def get_encryption_key() -> bytes:
    """Get the encryption key from settings."""
    if not settings.OPENAI_KEYS_ENCRYPTION_KEY:
        raise ValueError(
            "OPENAI_KEYS_ENCRYPTION_KEY environment variable must be set. "
            "Generate one with: python -c 'from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())'"
        )

    key = settings.OPENAI_KEYS_ENCRYPTION_KEY
    if isinstance(key, str):
        key = key.encode()

    return key


def encrypt_api_key(api_key: str) -> str:
    """Encrypt an API key using Fernet symmetric encryption.

    Args:
        api_key: The plaintext API key to encrypt

    Returns:
        The encrypted API key as a base64-encoded string
    """
    try:
        encryption_key = get_encryption_key()
        fernet = Fernet(encryption_key)
        encrypted = fernet.encrypt(api_key.encode())
        return encrypted.decode()
    except Exception as e:
        logger.error(f"Error encrypting API key: {e}")
        raise


def decrypt_api_key(encrypted_key: str) -> str:
    """Decrypt an API key using Fernet symmetric encryption.

    Args:
        encrypted_key: The encrypted API key as a base64-encoded string

    Returns:
        The decrypted plaintext API key
    """
    try:
        encryption_key = get_encryption_key()
        fernet = Fernet(encryption_key)
        decrypted = fernet.decrypt(encrypted_key.encode())
        return decrypted.decode()
    except Exception as e:
        logger.error(f"Error decrypting API key: {e}")
        raise


def mask_api_key(api_key: str) -> str:
    """Mask an API key for display purposes.

    Shows only the last 4 characters, replacing the rest with asterisks.

    Args:
        api_key: The API key to mask

    Returns:
        The masked API key (e.g., "sk-...xyz123")
    """
    if not api_key or len(api_key) < 8:
        return "****"

    if api_key.startswith("sk-"):
        return f"sk-...{api_key[-4:]}"

    return f"...{api_key[-4:]}"
