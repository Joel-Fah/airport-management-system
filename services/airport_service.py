import datetime
import time

from services.terminal_service import display_menu_terminal
from utils.constants import DEFAULT_SLEEP_TIME

AIRPORT_TABLE_NAME = "Airport"


def display_records_airport():
    """Displays all airports in the database."""
    from utils.db_utils import fetch_records
    from utils.utils import display_records

    # Fetch all airports from the database
    airports = fetch_records(table=AIRPORT_TABLE_NAME)
    print("\n")

    # Display the airports
    display_records(records=airports)

    if airports:
        # Ask for user input to select airport
        airport_id = input("Enter the ID of the airport to manage (or press enter to skip) >>> ").strip()

        if airport_id:
            # Fetch the airport record to manage
            airport_record = next((airport for airport in airports if airport["id"] == int(airport_id)), None)

            if airport_record:
                display_menu_terminal(airport_record=airport_record)
            else:
                print("\nAirport not found!")
                time.sleep(DEFAULT_SLEEP_TIME)
        else:
            pass
    else:
        time.sleep(DEFAULT_SLEEP_TIME)


def add_record_airport():
    """Adds a new airport to the database."""
    from utils.db_utils import insert_record

    # Ask for airport details
    airport_name = input("Enter airport name >>> ").strip()
    airport_location = input("Enter airport location >>> ").strip()
    airport_code = input("Enter airport code >>> ").strip()

    # Prepare the airport data
    airport_data = {
        "name": airport_name,
        "location": airport_location,
        "code": airport_code.upper(),
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now()
    }

    # Insert the airport record into the database
    insert_record(table=AIRPORT_TABLE_NAME, data=airport_data)
    time.sleep(DEFAULT_SLEEP_TIME)


def update_record_airport():
    """Updates an airport record in the database."""
    from utils.db_utils import fetch_records, update_record
    from utils.utils import display_records

    # Fetch all airports from the database
    airports = fetch_records(table=AIRPORT_TABLE_NAME)
    display_records(airports)

    # Ask for the airport ID to update
    airport_id = int(input("Enter the ID of the airport to update >>> ").strip())

    # Fetch the airport record to update
    airport_record = next((airport for airport in airports if airport["id"] == airport_id), None)

    if airport_record:
        # Ask for the new airport details
        new_name = input(f"Enter new name (leave blank to keep '{airport_record['name']}') >>> ").strip()
        new_location = input(f"Enter new location (leave blank to keep '{airport_record['location']}') >>> ").strip()
        new_code = input(f"Enter new code (leave blank to keep '{airport_record['code']}') >>> ").strip()

        # Prepare the new airport data
        new_data = {
            "name": new_name if new_name else airport_record["name"],
            "location": new_location if new_location else airport_record["location"],
            "code": new_code.upper() if new_code else airport_record["code"],
            "updated_at": datetime.datetime.now()
        }

        # Update the airport record in the database
        update_record(table=AIRPORT_TABLE_NAME, record_id=airport_id, new_data=new_data)
        time.sleep(DEFAULT_SLEEP_TIME)
    else:
        print("\nAirport not found!")
        time.sleep(DEFAULT_SLEEP_TIME)


def delete_record_airport():
    """Deletes an airport record from the database."""
    from utils.db_utils import delete_record, fetch_records
    from utils.utils import display_records

    # Fetch all airports from the database
    airports = fetch_records(table=AIRPORT_TABLE_NAME)

    # Display the airports
    display_records(records=airports)

    # Ask for the airport ID to delete
    airport_id = int(input("Enter the ID of the airport to delete >>> ").strip())

    if next((airport for airport in airports if airport["id"] == airport_id), None):
        # Delete the airport record from the database
        delete_record(table=AIRPORT_TABLE_NAME, record_id=airport_id)
        time.sleep(DEFAULT_SLEEP_TIME)
    else:
        print("\nAirport not found!")
        time.sleep(DEFAULT_SLEEP_TIME)


def display_menu__airport():
    """Displays the airport management menu."""
    from utils.utils import display_menu

    menu_title = "Airport Management"
    options = [
        "View Airports",
        "Add Airport",
        "Update Airport",
        "Delete Airport",
        "Back to Main Menu",
    ]

    while True:
        # Display airport management menu
        display_menu(menu_title=menu_title, options=options)

        # Ask for user input
        user_action = int(input(f"Enter your choice (1-{len(options)}) >>> ").strip())

        if user_action == 1:
            display_records_airport()
        elif user_action == 2:
            add_record_airport()
        elif user_action == 3:
            update_record_airport()
        elif user_action == 4:
            delete_record_airport()
        elif user_action == 5:
            break
        else:
            print(f"Invalid choice! Please enter a number between 1 and {len(options)}.")
            time.sleep(DEFAULT_SLEEP_TIME)
