# function to update user record in the database
import time

from utils.constants import DEFAULT_SLEEP_TIME
from utils.db_utils import update_record, fetch_records
from utils.logging_utils import validate_username, validate_email


def update_user_record(user_data):
    """
    Updates the user record in the database with the new details provided by the user.

    Args:
        user_data (dict): User details to update.

    Returns:
        bool: True if the user record was updated successfully, else False.
    """
    from utils.utils import clear_screen, display_menu_title

    # Clear the screen before showing the menu
    clear_screen()

    # Display the user details
    display_menu_title("Edit profile info")
    print("Current user details:")
    print(f"Username: {user_data['username']}")
    print(f"Email: {user_data['email']}", end="\n\n")

    # Ask for new details
    new_username = input("Enter new username (leave blank to keep current) >>> ").strip()
    # Validate the new username
    if new_username != '':
        while not validate_username(new_username):
            print("Invalid username. Please enter a valid username.")
            new_username = input("Enter new username (leave blank to keep current) >>> ").strip()

    new_email = input("Enter new email (leave blank to keep current) >>> ").strip()
    # Validate the new email
    if new_email != '':
        while not validate_email(new_email):
            print("Invalid email address. Please enter a valid email.")
            new_email = input("Enter new email (leave blank to keep current) >>> ").strip()


    new_data = {
        "username": new_username if new_username else user_data["username"],
        "email": new_email if new_email else user_data["email"],
    }

    # Update the user record in the database
    update_record("User", user_data["id"], new_data)

    time.sleep(DEFAULT_SLEEP_TIME)


def delete_user_record(user_id):
    """
    Deletes the user record from the database.

    Args:
        user_id (int): The ID of the user to delete. 

    Returns:
        bool: True if the user record was deleted successfully, else False.
    """
    from utils.db_utils import delete_record

    # Delete the user record from the database
    return delete_record("User", user_id)

def display_users():
    """
    Displays all the users in the database.
    """
    from utils.utils import display_records

    table = "User"
    fields = "id, username, email, role"

    all_users = fetch_records(table, fields=fields)
    display_records(all_users)