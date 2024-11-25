import datetime
import time

from services.flight_service import display_menu_flight
from utils.constants import DEFAULT_SLEEP_TIME

GATE_TABLE_NAME = "Gate"
GATE_DISPLAY_FIELDS = "id, gate_number, created_at, updated_at"


def display_records_gate(terminal_id: int):
    """Displays all gates in the database."""
    from utils.db_utils import fetch_records
    from utils.utils import display_records

    # Fetch all gates from the database
    gates = fetch_records(table=GATE_TABLE_NAME, fields=GATE_DISPLAY_FIELDS, filters={"terminal_id": terminal_id})
    print("\n")

    # Display the gates
    display_records(records=gates)

    if gates:
        # Ask for user input to select gate
        gate_id = input("Enter the ID of the gate to manage (or press enter to skip) >>> ").strip()

        if gate_id:
            # Fetch the gate record to manage
            gate_record = next((gate for gate in gates if gate["id"] == int(gate_id)), None)

            if gate_record:
                display_menu_flight(gate_record=gate_record)
        else:
            pass
    else:
        time.sleep(DEFAULT_SLEEP_TIME)


def add_record_gate(terminal_id):
    """Adds a new gate to the database."""
    from utils.db_utils import insert_record

    # Ask for gate details
    gate_number = input("Enter gate number (or gate name) >>> ").strip()

    # Prepare the gate data
    gate_data = {
        "gate_number": gate_number.upper(),
        "terminal_id": terminal_id,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now()
    }

    # Insert the gate record into the database
    insert_record(table=GATE_TABLE_NAME, data=gate_data)
    time.sleep(DEFAULT_SLEEP_TIME)


def update_record_gate(terminal_id: int):
    """Updates a gate record in the database."""
    from utils.db_utils import fetch_records, update_record
    from utils.utils import display_records

    # Fetch all gates from the database
    gates = fetch_records(table=GATE_TABLE_NAME, filters={"terminal_id": terminal_id})

    # Display the gates
    display_records(records=gates)

    # Ask for the gate ID to update
    gate_id = int(input("Enter the ID of the gate to update >>> ").strip())

    # Fetch the gate record from the database
    gate = next((g for g in gates if g["id"] == gate_id), None)

    if not gate:
        print("Gate not found.")
    else:
        # Ask for new details
        new_gate_number = input("Enter new gate number (leave blank to keep current) >>> ").strip()

        new_data = {
            "gate_number": new_gate_number.upper() if new_gate_number else gate["gate_number"],
            "updated_at": datetime.datetime.now()
        }

        # Update the gate record in the database
        update_record(table=GATE_TABLE_NAME, record_id=gate["id"], new_data=new_data)

        time.sleep(DEFAULT_SLEEP_TIME)


def delete_record_gate(terminal_id: int):
    """Deletes the gate record from the database."""
    from utils.db_utils import delete_record, fetch_records
    from utils.utils import display_records

    # Fetch all gates from the database
    gates = fetch_records(table=GATE_TABLE_NAME, filters={"terminal_id": terminal_id})

    # Display the gates
    display_records(records=gates)

    # Ask for the gate ID to delete
    gate_id = int(input("Enter the ID of the gate to delete >>> ").strip())

    # Fetch the gate record from the database
    gate = next((g for g in gates if g["id"] == gate_id), None)

    if not gate:
        print("Gate not found.")
    else:
        # Delete the gate record from the database
        delete_record(table=GATE_TABLE_NAME, record_id=gate_id)

        print("\nGate deleted successfully!")
        time.sleep(DEFAULT_SLEEP_TIME)


def display_menu_gate(terminal_record):
    """Displays the gate management menu."""
    from utils.utils import display_menu

    sub_menu_title = f"Manage Terminal: {terminal_record['name']}"
    sub_options = [
        "View gates",
        "Add gate",
        "Update gate",
        "Delete gate",
        "Back",
    ]

    while True:
        # Display gate management menu
        display_menu(menu_title=sub_menu_title, options=sub_options)

        # Ask for user input
        user_action = int(input(f"Enter your choice (1-{len(sub_options)}) >>> ").strip())

        if user_action == 1:
            display_records_gate(terminal_record['id'])
        elif user_action == 2:
            add_record_gate(terminal_record['id'])
        elif user_action == 3:
            update_record_gate(terminal_record['id'])
        elif user_action == 4:
            delete_record_gate(terminal_record['id'])
        elif user_action == 5:
            break
        else:
            print(f"Invalid choice! Please enter a number between 1 and {len(sub_options)}.")
            time.sleep(DEFAULT_SLEEP_TIME)
