import datetime
import time

from utils.constants import DEFAULT_SLEEP_TIME
from utils.utils import display_records

PASSENGER_TABLE_NAME = "Passenger"


def display_passengers():
    """Displays all passengers in the database."""
    from utils.db_utils import fetch_records

    # Fetch all passengers from the database
    passengers = fetch_records(PASSENGER_TABLE_NAME)
    print("\n")

    # Display the passengers
    display_records(passengers)

def add_new_passenger():
    pass

def update_passenger():
    pass

def delete_passenger():
    pass