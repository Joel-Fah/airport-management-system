import datetime
import os
import time

from services.airport_service import display_menu_airport
from services.user_service import update_user_record, display_users, delete_user_record
from utils.constants import DEFAULT_SLEEP_TIME


def clear_screen():
    """Clears the console screen."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')


def display_menu(menu_title, options):
    """Displays a beautifully styled menu and asks the user to choose an action.

    Args:
        menu_title (str): The title of the menu.
        options (list): A list of strings representing the menu options.

    Returns:
        str: The user's choice ('login', 'register', 'exit').

    Raises:
        ValueError: If the user enters an invalid choice.
    """

    # Clear the screen before showing the menu
    clear_screen()

    # Calculate the width of the box
    box_width = max(len(menu_title), max(len(opt) for opt in options) + 8)  # 8 accounts for padding and numbering.

    # Draw the top border
    print("+" + "-" * box_width + "+")
    print("|" + menu_title.center(box_width) + "|")
    print("+" + "-" * box_width + "+")

    # Display the menu options
    for i, option in enumerate(options, 1):
        print(f"| {i}. {option.ljust(box_width - 5)} |")  # Adjust padding for numbering.

    # Draw the bottom border
    print("+" + "-" * box_width + "+")


def display_menu_title(menu_title):
    """Displays a beautifully styled menu title.

    Args:
        menu_title (str): The title of the menu.
    """
    # Clear the screen before showing the menu
    clear_screen()

    # Calculate the width of the box
    box_width = len(menu_title) + 8  # 8 accounts for padding.

    # Draw the top border
    print("+" + "-" * box_width + "+")
    print("|" + menu_title.center(box_width) + "|")
    print("+" + "-" * box_width + "+")


def user_management_menu(user_data):
    """
    Sub menu to manage user related actions such as edit info, delete user, logout
    """

    # Clear the screen before showing the menu
    clear_screen()

    username = user_data['username']
    menu_title = f"AMS - User management ({username})"
    options = [
        "List All users",
        "Edit profile info",
        "Delete current user",
        "Back",
    ]

    while True:
        # display user management menu
        print("\n")
        display_menu(menu_title=menu_title, options=options)

        # Ask for user input
        user_action = int(input(f"Enter your choice (1-{len(options)}) >>> ").strip())

        if user_action == 1:
            display_users()
            close_input = input("Press enter to continue...")

            if close_input:
                continue
        elif user_action == 2:
            update_user_record(user_data=user_data)
        elif user_action == 3:
            delete_user_record(user_id=user_data['id'])
            time.sleep(DEFAULT_SLEEP_TIME)
        elif user_action == 4:
            break
        else:
            print(f"Invalid choice! Please enter a number between 1 and {len(options)}.")
            time.sleep(DEFAULT_SLEEP_TIME)


def main_menu(user_data):
    """Displays the main menu of the application."""
    menu_title = "Main menu"
    options = [
        "Airport Management",
        "User Management",
        "Logout",
    ]

    while True:
        clear_screen()

        # Display main menu
        display_menu(menu_title=menu_title, options=options)

        user_action = int(input(f"Select an option (1-{len(options)}) >>> ").strip())

        if user_action == 1:
            display_menu_airport()
        elif user_action == 2:
            user_management_menu(user_data)
        elif user_action == 3:
            print("Logging out...")
            break
        else:
            print(f"Invalid choice. Please enter a number between 1 and {len(options)}.")
            time.sleep(DEFAULT_SLEEP_TIME)


def display_records(records):
    """
    Displays records in a nicely formatted, en-boxed way.

    Args:
        records (list): A list of dictionaries representing the records.
    """
    if not records:
        print("No records found.")
        return

    # Get the column names from the first record
    columns = records[0].keys()
    column_widths = {col: max(len(col), max(len(str(record[col])) for record in records)) for col in columns}

    # Calculate the width of the box
    box_width = sum(column_widths.values()) + len(columns) * 3 + 1

    # Draw the top border
    print("+" + "-" * box_width + "+")

    # Print the header
    header = "| " + " | ".join(col.ljust(column_widths[col]) for col in columns) + " |"
    print(header)
    print("+" + "-" * box_width + "+")

    # Print each record row by row
    for record in records:
        row = "| " + " | ".join(str(record[col]).ljust(column_widths[col]) for col in columns) + " |"
        print(row)

    # Draw the bottom border
    print("+" + "-" * box_width + "+")


def date_formatter(date: datetime):
    """
    Converts the datetime object into an easily readable format.

    Args:
        date (datetime): The datetime object to be formatted.

    Returns:
        str: The formatted date string.
    """
    return time.strftime("%a. %d %b. %Y %H:%M")
