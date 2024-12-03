import hashlib
import re


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
    from utils.logging_utils import Role

    return role in [r.value for r in Role]


def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def validate_seat_number(seat_number: str):
    """
    Validates the seat number.

    Args:
        seat_number (str): The seat number to validate.

    Returns:
        bool: True if the seat number is valid, else False.
    """
    seat_regex = r'^[A-Z]([1-9]|[1-9][0-9]|100)$'
    return re.match(seat_regex, seat_number) is not None


def validate_passport_number(passport_number: str):
    """
    Validates the passport number.

    Args:
        passport_number (str): The passport number to validate.

    Returns:
        bool: True if the passport number is valid, else False.
    """
    passport_regex = r'^(?:[A-Z]{2}[0-9]{7}|[A-Z0-9]{9})$'
    return re.match(passport_regex, passport_number) is not None