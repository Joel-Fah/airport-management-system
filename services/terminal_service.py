import datetime
import time

from utils.constants import DEFAULT_SLEEP_TIME
from utils.utils import display_records

TERMINAL_TABLE_NAME = "Terminal"


def display_terminals():
    """Displays all terminals in the database."""
    from utils.db_utils import fetch_records

    # Fetch all terminals from the database
    terminals = fetch_records(table=TERMINAL_TABLE_NAME)
    print("\n")

    # Display the terminals
    display_records(records=terminals)


def add_new_terminal(airport_id):
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

    print("\nTerminal added successfully!")
    time.sleep(DEFAULT_SLEEP_TIME)


def update_terminal():
    """Updates a terminal record in the database."""
    from utils.db_utils import fetch_records, update_record

    # Fetch all terminals from the database
    terminals = fetch_records(table=TERMINAL_TABLE_NAME)

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

    print("\nTerminal updated successfully!")
    time.sleep(DEFAULT_SLEEP_TIME)


def delete_terminal_record():
    """Deletes a terminal record from the database."""
    from utils.db_utils import delete_record, fetch_records

    # Fetch all terminals from the database
    terminals = fetch_records(table=TERMINAL_TABLE_NAME)

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

        print("\nTerminal deleted successfully!")
        time.sleep(DEFAULT_SLEEP_TIME)
