import datetime
import time
from operator import indexOf

from utils.constants import DEFAULT_SLEEP_TIME
from utils.db_utils import connect_to_db

# Globals
TICKET_TABLE_NAME = "Ticket"
TICKET_DISPLAY_FIELDS = "id, ticket_number, seat_number, created_at, updated_at"
INITIAL_TICKET_NUMBER = "TICKET-0001"


def generate_ticket_number() -> str:
    """
    Generates a ticket number.

    Returns:
        str: The generated ticket number.
    """

    # Fetch the last ticket number from the database
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(f"SELECT ticket_number FROM {TICKET_TABLE_NAME} ORDER BY id DESC LIMIT 1")
    ticket_number = cursor.fetchone()
    connection.close()

    # Generate the new ticket number
    if ticket_number is None:
        return INITIAL_TICKET_NUMBER
    else:
        last_ticket_number = ticket_number[0]
        last_ticket_number = last_ticket_number.split("-")[1]
        new_ticket_number = int(last_ticket_number) + 1
        return f"TICKET-{str(new_ticket_number).zfill(4)}"


def get_valid_seat_number():
    """Gets a valid seat number from the user."""
    from utils.validation import validate_seat_number

    seat_number = input("Choose a seat number (A~Z)(1~100) e.g. B22 >>> ").strip()
    while not validate_seat_number(seat_number):
        print("Invalid seat number. Please try again.")
        seat_number = input("Choose a seat number (A~Z)(1~100) e.g. B22 >>> ").strip()
    return seat_number


def book_ticket(user_record_passenger: dict, flight_id: int):
    """
    Books a ticket for a passenger on a flight.

    Args:
        user_record_passenger (dict): The user record of the passenger.
        flight_id (int): The ID of the flight to book the ticket for.
    """
    from utils.db_utils import insert_record, fetch_records
    from utils.utils import display_menu_title
    from utils.validation import validate_passport_number

    # Generate the ticket number
    ticket_number = generate_ticket_number()

    # Ask for passport number
    passport_number = input("Enter passport number >>> ").strip()
    while not validate_passport_number(passport_number):
        print("Invalid passport number. Please enter a valid passport number.")
        passport_number = input("Enter passenger passport number >>> ").strip()

    # Nationality
    nationality = input("Enter your nationality >>> ").strip()

    # Ask for seat number
    seat_number = get_valid_seat_number()

    # Check if the seat is already booked
    tickets = fetch_records(table=TICKET_TABLE_NAME, fields="seat_number", filters={"flight_id": flight_id})
    booked_seats = [ticket["seat_number"] for ticket in tickets]

    while seat_number in booked_seats:
        print("Seat already booked. Please choose another seat.")
        seat_number = get_valid_seat_number()

    # Prepare the passenger data
    passenger_data = {
        "user_id": user_record_passenger["id"],
        "name": user_record_passenger["username"],
        "passport_number": passport_number.upper(),
        "nationality": nationality,
        "flight_id": flight_id,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now()
    }

    # Insert passenger record into the database
    passenger_id = insert_record(table="Passenger", data=passenger_data)

    # Prepare the ticket data
    ticket_data = {
        "ticket_number": ticket_number,
        "seat_number": seat_number,
        "passenger_id": user_record_passenger["id"],
        "flight_id": flight_id,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now()
    }

    # Insert the ticket record into the database
    ticket_id = insert_record(table=TICKET_TABLE_NAME, data=ticket_data)

    # Display the ticket details
    print("\n")
    display_menu_title(menu_title="Ticket booked successfully", clear_scr=False)
    print("\n")
    # display_records(records=[ticket_data])
    display_ticket_info(ticket_id)

    time.sleep(DEFAULT_SLEEP_TIME)


def display_records_ticket(user_record_passenger_id: int):
    """
    Displays all tickets of a passenger.

    Args:
        user_record_passenger_id (dict): The user record of the passenger.
    """

    from utils.db_utils import fetch_records
    from utils.utils import display_menu_title

    # Fetch the passenger with the given user ID
    # passenger_id = fetch_records(table="Passenger", fields="id", filters={"user_id": user_record_passenger_id})[0]["id"]

    # Fetch all tickets from the database
    tickets = fetch_records(table=TICKET_TABLE_NAME,
                            filters={"passenger_id": user_record_passenger_id},)
    print("\n")

    # List of ticket Ids
    ticket_ids = [ticket["id"] for ticket in tickets]

    display_menu_title(menu_title=f"Total tickets booked: {len(tickets)}", clear_scr=False)
    print("\n")

    # Display the tickets
    for ticket_id in ticket_ids:
        print(f"Ticket {indexOf(ticket_ids, ticket_id) + 1}")
        display_ticket_info(ticket_id)
        print("\n")


def display_ticket_info(ticket_id: int):
    """
    Displays the ticket information along with related passenger, flight, and gate details.

    Args:
        ticket_id (int): The ID of the ticket to display.
    """
    from utils.utils import display_records

    connection = connect_to_db(echo=False)
    cursor = connection.cursor()

    query = """
    SELECT
        Ticket.ticket_number,
        Ticket.seat_number,
        Passenger.name,
        Passenger.passport_number,
        Flight.flight_number,
        Flight.origin,
        Flight.destination,
        Flight.departure_time,
        Flight.arrival_time,
        Gate.gate_number
    FROM Ticket
    JOIN Passenger ON Ticket.passenger_id = Passenger.id
    JOIN Flight ON Ticket.flight_id = Flight.id
    JOIN Gate ON Flight.gate_id = Gate.id
    WHERE Ticket.id = ?
    """

    cursor.execute(query, (ticket_id,))
    ticket_info = cursor.fetchone()
    connection.close()

    if ticket_info:
        ticket_dict = {
            "ticket_number": ticket_info[0],
            "seat_number": ticket_info[1],
            "passenger_name": ticket_info[2],
            "passport_number": ticket_info[3],
            "flight_number": ticket_info[4],
            "origin": ticket_info[5],
            "destination": ticket_info[6],
            "departure_time": ticket_info[7],
            "arrival_time": ticket_info[8],
            "gate_number": ticket_info[9]
        }
        display_records([ticket_dict])
    else:
        print("No ticket found with the given ID.")
