import hashlib
import re

from utils.logging_utils import Role


def validate_username(username):
    """Validates the username.

    Args:
        username (str): The username to validate.

    Returns:
        bool: True if the username is valid, else False.
    """
    return username.isalnum() and 4 <= len(username) <= 20


def validate_email(email):
    """Validates the email address using regex.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email address is valid, else False.
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None


def validate_password(password):
    """Validates the password.

    Args:
        password (str): The password to validate.

    Returns:
        bool: True if the password is valid, else False.
    """
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password):
        return False
    return True


def validate_role(role):
    """Validates the role.

    Args:
        role (str): The role to validate.

    Returns:
        bool: True if the role is valid, else False.
    """
    return role in [r.value for r in Role]


def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()
