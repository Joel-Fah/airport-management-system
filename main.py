# Main entry point for the application
import time

from utils.constants import DEFAULT_SLEEP_TIME
from utils.db_utils import create_tables
from utils.utils import display_menu
from utils.logging_utils import register_user, login_user

def initialise_system():
    """
    Initialises the project's database, ensuring the tables are created and ready to use upfront.
    """
    print("Initializing the Airport Management System...")

    # Create tables (if not already created)
    create_tables()

    # small delay before proceeding
    time.sleep(DEFAULT_SLEEP_TIME / 3)

def main():
    """Main entry point of the application."""
    # Main program loop
    while True:
        display_menu(
            "Welcome to Airport Management System. Login or Register",
            ["Login", "Register", "Exit"]
        )

        # Ask for user input
        user_action = int(input("Enter your choice (1-3) >>> ").strip())

        if user_action == 1:
            login_user()
            time.sleep(DEFAULT_SLEEP_TIME)
        elif user_action == 2:
            register_user()
        elif user_action == 3:
            print("\nThank you for using the Airport Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 3.")
            time.sleep(1)


if __name__ == "__main__":
    initialise_system()
    main()