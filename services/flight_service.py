# display flight menu
import datetime
import time

from utils.constants import DEFAULT_SLEEP_TIME
from utils.utils import display_records

# Globals
FLIGHT_TABLE_NAME = "Flight"


def display_flights():
    """Displays all flights in the database."""
    from utils.db_utils import fetch_records

    # Fetch all flights from the database
    flights = fetch_records(FLIGHT_TABLE_NAME)

    # Display the flights
    display_records(flights)


def add_new_flight():
    """Adds a new flight to the database."""
    from utils.db_utils import insert_record

    # Ask for flight details
    flight_number = input("Enter flight number >>> ").strip()
    origin = input("Enter departure location >>> ").strip()
    destination = input("Enter destination location >>> ").strip()
    departure_time = input("Enter departure time (YYYY-MM-DD HH:MM) >>> ").strip()
    arrival_time = input("Enter arrival time (YYYY-MM-DD HH:MM) >>> ").strip()
    price = input("Enter price >>> ").strip()

    # Prepare the flight data
    flight_data = {
        "flight_number": flight_number,
        "origin": origin,
        "destination": destination,
        "departure_time": departure_time,
        "arrival_time": arrival_time,
        "price": price,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now()
    }

    # Insert the flight record into the database
    insert_record(table=FLIGHT_TABLE_NAME, data=flight_data)

    print("\nFlight added successfully!")
    time.sleep(DEFAULT_SLEEP_TIME)


def update_flight():
    """Updates a flight record in the database."""
    from utils.db_utils import fetch_records, update_record

    # Fetch all flights from the database
    flights = fetch_records(table=FLIGHT_TABLE_NAME)

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
    price = input(f"Enter new price (leave blank to keep current: {flight['price']}) >>> ").strip()

    # Prepare the new flight data
    new_data = {
        "flight_number": flight_number if flight_number else flight["flight_number"],
        "origin": origin if origin else flight["origin"],
        "destination": destination if destination else flight["destination"],
        "departure_time": departure_time if departure_time else flight["departure_time"],
        "arrival_time": arrival_time if arrival_time else flight["arrival_time"],
        "price": price if price else flight["price"],
        "updated_at": datetime.datetime.now()
    }

    # Update the flight record in the database
    update_record(table=FLIGHT_TABLE_NAME, record_id=flight_id, new_data=new_data)

    print("\nFlight updated successfully!")
    time.sleep(DEFAULT_SLEEP_TIME)


def delete_flight():
    """Deletes a flight record from the database."""
    from utils.db_utils import delete_record, fetch_records

    # Fetch all flights from the database
    flights = fetch_records(table=FLIGHT_TABLE_NAME)

    # Display the flights
    display_records(records=flights)

    # Ask for the flight ID to delete
    flight_id = int(input("Enter the ID of the flight to delete >>> ").strip())

    # Delete the flight record from the database
    delete_record(table=FLIGHT_TABLE_NAME, record_id=flight_id)

    print("\nFlight deleted successfully!")
    time.sleep(DEFAULT_SLEEP_TIME)


def display_flight_menu():
    """Displays the flight management menu."""
    from utils.utils import display_menu

    menu_title = "Flight Management"
    options = [
        "View all flights",
        "Add a new flight",
        "Edit a flight",
        "Delete a flight",
        "Back to main menu",
    ]

    while True:
        # display flight management menu
        print("\n")
        display_menu(menu_title=menu_title, options=options)

        # Ask for user input
        user_action = int(input(f"Enter your choice (1-{len(options)}) >>> ").strip())

        if user_action == 1:
            display_flights()
            close_input = input("Press enter to continue...")

            if close_input:
                continue
        elif user_action == 2:
            add_new_flight()
        elif user_action == 3:
            update_flight()
        elif user_action == 4:
            delete_flight()
        elif user_action == 5:
            break
        else:
            print(f"Invalid choice! Please enter a number between 1 and {len(options)}.")
            time.sleep(DEFAULT_SLEEP_TIME)
