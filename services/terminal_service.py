import datetime
import time

from services.gate_service import display_menu_gate
from utils.constants import DEFAULT_SLEEP_TIME

TERMINAL_TABLE_NAME = "Terminal"
TERMINAL_DISPLAY_FIELDS = "id, name, created_at, updated_at"


def display_records_terminal(airport_id: int):
    """Displays all terminals in the database."""
    from utils.utils import display_records

    from utils.db_utils import fetch_records

    # Fetch all terminals of the specified airport from the database
    terminals = fetch_records(table=TERMINAL_TABLE_NAME, fields=TERMINAL_DISPLAY_FIELDS,
                              filters={"airport_id": airport_id})

    print("\n")
    # Display the terminals
    display_records(records=terminals)

    if terminals:
        # Ask for user input to select terminal
        terminal_id = input("Enter the ID of the terminal to manage (or press enter to skip) >>> ").strip()

        if terminal_id:
            # Fetch the terminal record to manage
            terminal_record = next((terminal for terminal in terminals if terminal["id"] == int(terminal_id)), None)

            if terminal_record:
                display_menu_gate(terminal_record=terminal_record)
        else:
            pass
    else:
        time.sleep(DEFAULT_SLEEP_TIME)


def add_record_terminal(airport_id):
    """Adds a new terminal to the database."""
    from utils.db_utils import insert_record

    # Ask for terminal details
    terminal_name = input("Enter terminal name >>> ").strip()

    # Prepare the terminal data
    terminal_data = {
        "name": terminal_name,
        "airport_id": airport_id,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now()
    }

    # Insert the terminal record into the database
    insert_record(table=TERMINAL_TABLE_NAME, data=terminal_data)
    time.sleep(DEFAULT_SLEEP_TIME)


def update_record_terminal(airport_id: int):
    """Updates a terminal record in the database."""
    from utils.db_utils import fetch_records, update_record
    from utils.utils import display_records

    # Fetch all terminals from the database
    terminals = fetch_records(table=TERMINAL_TABLE_NAME, fields=TERMINAL_DISPLAY_FIELDS,
                              filters={"airport_id": airport_id})

    # Display the terminals
    display_records(records=terminals)

    # Ask for the terminal ID to update
    terminal_id = int(input("Enter the ID of the terminal to update >>> ").strip())

    # Fetch the terminal record from the database
    terminal = next((t for t in terminals if t["id"] == terminal_id), None)

    if not terminal:
        print("Terminal not found.")
        time.sleep(DEFAULT_SLEEP_TIME)
        return

    # Ask for the new terminal name
    new_terminal_name = input("Enter new terminal name >>> ").strip()

    # Prepare the new terminal data
    new_terminal_data = {
        "name": new_terminal_name,
        "updated_at": datetime.datetime.now()
    }

    # Update the terminal record in the database
    update_record(table=TERMINAL_TABLE_NAME, record_id=terminal_id, new_data=new_terminal_data)
    time.sleep(DEFAULT_SLEEP_TIME)


def delete_record_terminal(airport_id: int):
    """Deletes a terminal record from the database."""
    from utils.db_utils import delete_record, fetch_records
    from utils.utils import display_records

    # Fetch all terminals from the database
    terminals = fetch_records(table=TERMINAL_TABLE_NAME, fields=TERMINAL_DISPLAY_FIELDS,
                              filters={"airport_id": airport_id})

    # Display the terminals
    display_records(records=terminals)

    # Ask for the terminal ID to delete
    terminal_id = int(input("Enter the ID of the terminal to delete >>> ").strip())

    # Fetch the terminal record from the database
    terminal = next((t for t in terminals if t["id"] == terminal_id), None)

    if not terminal:
        print("Terminal not found.")
        time.sleep(DEFAULT_SLEEP_TIME)
        return
    else:
        # Delete the terminal record from the database
        delete_record(table=TERMINAL_TABLE_NAME, record_id=terminal_id)
        time.sleep(DEFAULT_SLEEP_TIME)


def display_menu_terminal(airport_record):
    """Displays the terminal management menu."""
    from utils.utils import display_menu

    sub_menu_title = f"Manage {airport_record['name']}"
    sub_options = [
        "View terminals",
        "Add terminal",
        "Update terminal",
        "Delete terminal",
        "Back",
    ]

    while True:
        # Display terminal management menu
        display_menu(menu_title=sub_menu_title, options=sub_options)

        # Ask for user input
        user_action = int(input(f"Enter your choice (1-{len(sub_options)}) >>> ").strip())

        if user_action == 1:
            display_records_terminal(airport_record['id'])
        elif user_action == 2:
            add_record_terminal(airport_record['id'])
        elif user_action == 3:
            update_record_terminal(airport_record['id'])
        elif user_action == 4:
            delete_record_terminal(airport_record['id'])
        elif user_action == 5:
            break
        else:
            print(f"Invalid choice! Please enter a number between 1 and {len(sub_options)}.")
            time.sleep(DEFAULT_SLEEP_TIME)
