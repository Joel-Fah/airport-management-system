import os


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

    # Ask for user input
    try:
        choice = int(input("Enter your choice (1-3) >>> ").strip())
        if choice == 1:
            return "login"
        elif choice == 2:
            return "register"
        elif choice == 3:
            return "exit"
        else:
            raise ValueError
    except ValueError:
        print("Invalid choice! Please enter a number between 1 and 3.")
        return display_menu(menu_title, options)  # Recurse to display the menu again for valid input.


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