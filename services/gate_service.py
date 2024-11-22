import datetime
import time

from utils.constants import DEFAULT_SLEEP_TIME
from utils.utils import display_records

TERMINAL_TABLE_NAME = "Gate"

def display_gates():
    """Displays all gates in the database."""
    from utils.db_utils import fetch_records

    # Fetch all gates from the database
    gates = fetch_records(table=TERMINAL_TABLE_NAME)
    print("\n")

    # Display the gates
    display_records(records=gates)

def add_new_gate(terminal_id):
    """Adds a new gate to the database."""
    from utils.db_utils import insert_record

    # Ask for gate details
    gate_number = input("Enter gate number >>> ").strip()

    # Prepare the gate data
    gate_data = {
        "gate_number": gate_number,
        "terminal_id": terminal_id,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now()
    }

    # Insert the gate record into the database
    insert_record(table=TERMINAL_TABLE_NAME, data=gate_data)

    print("\nGate added successfully!")
    time.sleep(DEFAULT_SLEEP_TIME)

def update_gate():
    """Updates a gate record in the database."""
    from utils.db_utils import fetch_records, update_record

    # Fetch all gates from the database
    gates = fetch_records(table=TERMINAL_TABLE_NAME)

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
            "gate_number": new_gate_number if new_gate_number else gate["gate_number"],
            "updated_at": datetime.datetime.now()
        }

        # Update the gate record in the database
        update_record(table=TERMINAL_TABLE_NAME, record_id=gate["id"], new_data=new_data)

        time.sleep(DEFAULT_SLEEP_TIME)

def delete_gate_record():
    """Deletes the gate record from the database."""
    from utils.db_utils import delete_record, fetch_records

    # Fetch all gates from the database
    gates = fetch_records(table=TERMINAL_TABLE_NAME)

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
        delete_record(table=TERMINAL_TABLE_NAME, record_id=gate_id)

        print("\nGate deleted successfully!")
        time.sleep(DEFAULT_SLEEP_TIME)