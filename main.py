# Main entry point for the application
import time

from utils.constants import DEFAULT_SLEEP_TIME
from utils.logging_utils import register_user, login_user
from utils.utils import display_menu, initialise_system


def main():
    """Main entry point of the application."""
    # Main program loop
    while True:
        display_menu(
            menu_title="Welcome to Airport Management System. Login or Register",
            options=["Login", "Register", "Exit"]
        )

        # Ask for user input
        user_action = int(input("Enter your choice (1-3) >>> ").strip())

        if user_action == 1:
            login_user()
            time.sleep(DEFAULT_SLEEP_TIME)
        elif user_action == 2:
            register_user()
        elif user_action == 3:
            #  services_main_menu()
            print("\nThank you for using the Airport Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 3.")
            time.sleep(1)


if __name__ == "__main__":
    initialise_system()
    main()
