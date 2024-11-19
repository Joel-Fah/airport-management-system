import os
import time

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

    while True:
        # display user management menu
        display_menu(
            f" AMS - User management ({username})",
            [
                "Edit profile info",
                "Delete user",
            ]
        )

        # Ask for user input
        user_action = int(input("Enter your choice (1-3) >>> ").strip())

        if user_action == 1:
            # Update user record
            pass
        elif user_action == 2:
            # Delete user record
            pass
        else:
            print("Invalid choice! Please enter a number between 1 and 3.")

def main_menu(user_data):
    """Displays the main menu of the application."""
    while True:
        clear_screen()

        # Display main menu
        display_menu(
            "Main Menu",
            [
                "Airport Management",
                "User Management",
                "Logout"
            ]
        )

        user_action = int(input("Select an option >>> ").strip())

        if user_action == 1:
            # Handle Option 1
            pass
        elif user_action == 2:
            user_management_menu(user_data)
        elif user_action == 3:
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")