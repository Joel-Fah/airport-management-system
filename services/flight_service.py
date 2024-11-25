import datetime
import time

from utils.constants import DEFAULT_SLEEP_TIME

# Globals
FLIGHT_TABLE_NAME = "Flight"
FLIGHT_DISPLAY_FIELDS = "id, flight_number, origin, destination, departure_time, arrival_time, created_at, updated_at"


def display_records_flight(gate_id: int):
    """Displays all flights in the database."""
    from utils.db_utils import fetch_records
    from utils.utils import display_records

    # Fetch all flights from the database
    flights = fetch_records(table=FLIGHT_TABLE_NAME, fields=FLIGHT_DISPLAY_FIELDS, filters={"gate_id": gate_id})
    print("\n")

    # Display the flights
    display_records(flights)


def add_record_flight(gate_id: int):
    """Adds a new flight to the database."""
    from utils.db_utils import insert_record

    # Ask for flight details
    flight_number = input("Enter flight number >>> ").strip()
    origin = input("Enter departure location >>> ").strip()
    destination = input("Enter destination location >>> ").strip()
    departure_time = input("Enter departure time (YYYY-MM-DD HH:MM) >>> ").strip()
    arrival_time = input("Enter arrival time (YYYY-MM-DD HH:MM) >>> ").strip()

    # Prepare the flight data
    flight_data = {
        "flight_number": flight_number.upper(),
        "origin": origin,
        "destination": destination,
        "departure_time": departure_time,
        "arrival_time": arrival_time,
        "gate_id": gate_id,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now()
    }

    # Insert the flight record into the database
    insert_record(table=FLIGHT_TABLE_NAME, data=flight_data)
    time.sleep(DEFAULT_SLEEP_TIME)


def update_record_flight(gate_id: int):
    """Updates a flight record in the database."""
    from utils.db_utils import fetch_records, update_record
    from utils.utils import display_records

    # Fetch all flights from the database
    flights = fetch_records(table=FLIGHT_TABLE_NAME, fields=FLIGHT_DISPLAY_FIELDS, filters={"gate_id": gate_id})

    # Display the flights
    display_records(records=flights)

    # Ask for the flight ID to update
    flight_id = int(input("Enter the ID of the flight to update >>> ").strip())

    # Fetch the flight record from the database
    flight = fetch_records(table=FLIGHT_TABLE_NAME, filters={"id": flight_id})[0]

    # Ask for the new flight details
    flight_number = input(
        f"Enter new flight number (leave blank to keep current: {flight['flight_number']}) >>> ").strip()
    origin = input(f"Enter new departure location (leave blank to keep current: {flight['origin']}) >>> ").strip()
    destination = input(
        f"Enter new destination location (leave blank to keep current: {flight['destination']}) >>> ").strip()
    departure_time = input(
        f"Enter new departure time (YYYY-MM-DD HH:MM) (leave blank to keep current: {flight['departure_time']}) >>> ").strip()
    arrival_time = input(
        f"Enter new arrival time (YYYY-MM-DD HH:MM) (leave blank to keep current: {flight['arrival_time']}) >>> ").strip()

    # Prepare the new flight data
    new_data = {
        "flight_number": flight_number.upper() if flight_number else flight["flight_number"],
        "origin": origin if origin else flight["origin"],
        "destination": destination if destination else flight["destination"],
        "departure_time": departure_time if departure_time else flight["departure_time"],
        "arrival_time": arrival_time if arrival_time else flight["arrival_time"],
        "updated_at": datetime.datetime.now()
    }

    # Update the flight record in the database
    update_record(table=FLIGHT_TABLE_NAME, record_id=flight_id, new_data=new_data)
    time.sleep(DEFAULT_SLEEP_TIME)


def delete_record_flight(gate_id: int):
    """Deletes a flight record from the database."""
    from utils.db_utils import delete_record, fetch_records
    from utils.utils import display_records

    # Fetch all flights from the database
    flights = fetch_records(table=FLIGHT_TABLE_NAME, fields=FLIGHT_DISPLAY_FIELDS, filters={"gate_id": gate_id})

    # Display the flights
    display_records(records=flights)

    # Ask for the flight ID to delete
    flight_id = int(input("Enter the ID of the flight to delete >>> ").strip())

    # Delete the flight record from the database
    delete_record(table=FLIGHT_TABLE_NAME, record_id=flight_id)
    time.sleep(DEFAULT_SLEEP_TIME)


def display_menu_flight(gate_record):
    """Displays the flight management menu."""
    from utils.utils import display_menu

    menu_title = f"Manage Flight: Gate {gate_record['gate_number']}"
    options = [
        "View flight",
        "Add a new flight",
        "Edit a flight",
        "Delete a flight",
        "Back",
    ]

    while True:
        # display flight management menu
        print("\n")
        display_menu(menu_title=menu_title, options=options)

        # Ask for user input
        user_action = int(input(f"Enter your choice (1-{len(options)}) >>> ").strip())

        if user_action == 1:
            display_records_flight(gate_record['id'])
            close_input = input("Press enter to continue...")

            if close_input:
                continue
        elif user_action == 2:
            add_record_flight(gate_record['id'])
        elif user_action == 3:
            update_record_flight(gate_record['id'])
        elif user_action == 4:
            delete_record_flight(gate_record['id'])
        elif user_action == 5:
            break
        else:
            print(f"Invalid choice! Please enter a number between 1 and {len(options)}.")
            time.sleep(DEFAULT_SLEEP_TIME)
