import hashlib
import re
import sqlite3
import time
from enum import Enum

from .constants import DEFAULT_SLEEP_TIME
from .db_utils import connect_to_db, close_connection


class Role(Enum):
    ADMIN = "Admin"
    STAFF = "Staff"
    GUEST = "Guest"

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


def register_user():
    """Registers a new user in the system.

    Raises:
        ValueError: If the username is already taken.
        ValueError: If the provided role is invalid.
    """
    from .utils import display_menu_title, clear_screen

    # Clear the screen before showing the menu
    clear_screen()

    # Prompt the user to enter their username, email, password, and select role
    display_menu_title("Register")
    username = input("Enter your username >>> ").strip()
    while not validate_username(username):
        print("Invalid username. Please enter an alphanumeric username between 4 and 20 characters.")
        username = input("Enter your username >>> ").strip()

    email = input("Enter your email >>> ").strip()
    while not validate_email(email):
        print("Invalid email address. Please enter a valid email.")
        email = input("Enter your email >>> ").strip()

    password = input("Enter your password >>> ").strip()
    while not validate_password(password):
        print("Invalid password. Password must be at least 8 characters long, contain at least one uppercase letter, one number, and one special character.")
        password = input("Enter your password >>> ").strip()

    confirm_password = input("Confirm your password >>> ").strip()
    while password != confirm_password:
        print("Passwords do not match. Please try again.")
        confirm_password = input("Confirm your password >>> ").strip()

    input_role = input("Select your role (Admin, Staff, Guest) >>> ").strip().capitalize()
    while not validate_role(input_role):
        print("Invalid role. Please choose from the following:")
        for role in Role:
            print(f"- {role.value.capitalize()}")
        input_role = input("Select your role (Admin, Staff, Guest) >>> ").strip().capitalize()
    role = Role[input_role.upper()]

    connection = connect_to_db()
    if not connection:
        print("Failed to connect to the database.")
        return

    try:
        cursor = connection.cursor()

        # Check for duplicate username
        cursor.execute("SELECT id FROM User WHERE username = ?", (username,))
        if cursor.fetchone():
            raise ValueError("Username already exists. Please choose a different one.")

        # Hash the password
        hashed_password = hash_password(password)

        # Insert new user
        query = """
            INSERT INTO User (username, email, password, role)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(query, (username, email, hashed_password, role.value))
        connection.commit()
        print(f"User '{username}' registered successfully.")

        # small delay before proceeding
        time.sleep(DEFAULT_SLEEP_TIME)

        # Login user
        login_user()
    except sqlite3.Error as e:
        print(f"Error registering user: {e}")
    finally:
        close_connection(connection)


def login_user():
    """Logs in a user with the given username and password.

    Returns:
        dict: User details if login is successful, else None.

    Raises:
        ValueError: If the username or password is incorrect.
    """
    from .utils import display_menu_title, clear_screen, main_menu

    # Clear the screen before showing the menu
    clear_screen()

    # Prompt the user to enter their username and password
    display_menu_title("Login")
    username = input("Enter your username >>> ").strip()
    password = input("Enter your password >>> ").strip()

    connection = connect_to_db()
    if not connection:
        print("Failed to connect to the database.")
        return

    try:
        cursor = connection.cursor()

        # Hash the password
        hashed_password = hash_password(password)

        # Verify username and password
        query = """
            SELECT id, username, email, role
            FROM User
            WHERE username = ? AND password = ?
        """
        cursor.execute(query, (username, hashed_password))
        user = cursor.fetchone()

        if not user:
            print("Incorrect username or password.")
            return

        # Return user details
        user_data = {
            "id": user[0],
            "username": user[1],
            "email": user[2],
            "role": user[3],
        }
        print(f"Logged in as '{user_data['username']}' ({user_data['role']})")

        # Go to main menu
        main_menu(user_data)
        # return user_data
    except sqlite3.Error as e:
        print(f"Error logging in: {e}")
    finally:
        close_connection(connection)