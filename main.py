# Main entry point for the application
import time

from utils.db_utils import create_tables
from utils.utils import display_menu
from utils.logging_utils import register_user, login_user

def main():
    """Main entry point of the application."""
    print("Initializing the Airport Management System...")

    # Step 1: Create tables (if not already created)
    create_tables()

    # small delay
    time.sleep(1)
    
    # Step 2: Main program loop
    while True:
        user_action = display_menu(
            " Airport Management System ",
            ["Login", "Register", "Exit"]
        )

        if user_action == "login":
            login_user()
        elif user_action == "register":
            register_user()
        elif user_action == "exit":
            print("\nThank you for using the Airport Management System. Goodbye!")
            break

if __name__ == "__main__":
    main()
