import datetime
import time

from utils.constants import DEFAULT_SLEEP_TIME
from utils.utils import display_records

PASSENGER_TABLE_NAME = "Passenger"


def display_flight_passengers(flight_id: int):
    """Displays all passengers in the database."""
    from utils.db_utils import fetch_records

    # Fetch all passengers from the database
    passengers = fetch_records(PASSENGER_TABLE_NAME)
    print("\n")

    # Display the passengers
    display_records(passengers)

def add_new_passenger_to_flight(flight_id: int):
    """Adds a new passenger to the database."""
    from utils.db_utils import insert_record

    # Ask for passenger details
    name = input("Enter passenger name >>> ").strip()
    passport = input("Enter passenger passport >>> ").strip()
    nationality = input("Enter passenger nationality >>> ").strip()

    # Prepare the passenger data
    passenger_data = {
        "name": name,
        "passport": passport,
        "nationality": nationality,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now()
    }

    # Insert the passenger record into the database
    insert_record(table=PASSENGER_TABLE_NAME, data=passenger_data)

    print("\nPassenger added successfully!")
    time.sleep(DEFAULT_SLEEP_TIME)

def update_passenger():
    """Updates a passenger record in the database."""
    from utils.db_utils import fetch_records, update_record
    from utils.utils import display_records

    # Fetch all passengers from the database
    passengers = fetch_records(table=PASSENGER_TABLE_NAME)
    display_records(passengers)

    # Ask for the passenger ID to update
    passenger_id = int(input("Enter the ID of the passenger to update >>> ").strip())

    # Fetch the passenger record to update
    passenger_record = next((passenger for passenger in passengers if passenger["id"] == passenger_id), None)

    # Check if the passenger record exists
    if not passenger_record:
        print("Passenger not found!")
        time.sleep(DEFAULT_SLEEP_TIME)
        return
    else:
        print("\nCurrent passenger details:")
        display_records(records=[passenger_record])

        # Ask for new details
        new_name = input("Enter new name (leave blank to keep current) >>> ").strip()
        new_passport = input("Enter new passport (leave blank to keep current) >>> ").strip
        new_nationality = input("Enter new nationality (leave blank to keep current) >>> ").strip()

        new_data = {
            "name": new_name if new_name else passenger_record["name"],
            "passport": new_passport if new_passport else passenger_record["passport"],
            "nationality": new_nationality if new_nationality else passenger_record["nationality"],
            "updated_at": datetime.datetime.now()
        }

        # Update the passenger record in the database
        update_record(table=PASSENGER_TABLE_NAME, record_id=passenger_record["id"], new_data=new_data)

        print("\nPassenger updated successfully!")
        time.sleep(DEFAULT_SLEEP_TIME)

def delete_passenger_record():
    """
    Deletes the passenger record from the database.
    """
    from utils.db_utils import delete_record, fetch_records

    # Fetch all passengers from the database
    passengers = fetch_records(table=PASSENGER_TABLE_NAME)

    # Display the passengers
    display_records(records=passengers)

    # Ask for the passenger ID to delete
    passenger_id = int(input("Enter the ID of the passenger to delete >>> ").strip())

    if next((passenger for passenger in passengers if passenger["id"] == passenger_id), None):
        # Delete the passenger record from the database
        delete_record(table=PASSENGER_TABLE_NAME, record_id=passenger_id)

        print("\nPassenger deleted successfully!")
        time.sleep(DEFAULT_SLEEP_TIME)
    else:
        print("\nPassenger not found!")
        time.sleep(DEFAULT_SLEEP_TIME)

