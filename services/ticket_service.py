import datetime
import time
from utils.constants import DEFAULT_SLEEP_TIME
from services.flight_service import display_menu_flight

TICKET_TABLE_NAME="Ticket"
TICKET_DISPLAY_FIELDS = "id, passenger_name,flight_id, created_at, updated_at"


def display_ticket_records(ticket_id: int):
    """Displays all ticket in the database."""
    from utils.utils import display_records

    from utils.db_utils import fetch_records

    # Fetch all ticket of the specified airport from the database
    tickets= fetch_records(table=TICKET_TABLE_NAME, fields=TICKET_DISPLAY_FIELDS,
                              filters={"ticket_id": ticket_id})

    print("\n")
    # Display the ticket
    display_records(records=tickets)

    if tickets:
        # Ask for user input to select ticket
        ticket_id = input("Enter the ID of the ticket to manage (or press enter to skip) >>> ").strip()

        if ticket_id:
            # Fetch the ticket record to manage
            ticket_record = next((ticket for ticket in tickets if ticket["id"] == int(ticket_id)), None)

            if ticket_record:
                display_menu_flight(ticket_record=ticket_record)
        else:
            pass
    else:
        time.sleep(DEFAULT_SLEEP_TIME)


def add_ticket_record(ticket_id):
    """Adds a new ticket to the database."""
    from utils.db_utils import insert_record

    # Ask for terminal details
    passenger_name= input("Enter passenger name >>> ").strip()
    flight_id= input("Enter the flight id >>> ").strip()
    seat_number= input("Enter seat number >>> ").strip()
    ticket_number=input("Enter ticket number >>> ").strip()

    # Prepare the ticket data
    ticket_data = {
        "passenger_name": passenger_name,
        "flight_id": flight_id,
        "seat_number":seat_number,
        "ticket_number":ticket_number,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now()
    }

    # Insert the terminal record into the database
    insert_record(table=TICKET_TABLE_NAME, data=ticket_data)
    time.sleep(DEFAULT_SLEEP_TIME)


def update_ticket_record(ticket_id: int):
    """Updates a ticket record in the database."""
    from utils.db_utils import fetch_records, update_record
    from utils.utils import display_records

    # Fetch all ticket from the database
    tickets = fetch_records(table=TICKET_TABLE_NAME, fields=TICKET_DISPLAY_FIELDS,
                              filters={"ticket_id": ticket_id})

    # Display the ticket
    display_records(records=tickets)

    # Ask for the ticket ID to update
    ticket_id = int(input("Enter the ID of the ticket to update >>> ").strip())

    # Fetch the ticket record from the database
    ticket = next((t for t in ticket if t["id"] == ticket_id), None)

    if not ticket:
        print("Ticket not found.")
        time.sleep(DEFAULT_SLEEP_TIME)
        return

    # Ask for data to modify
    new_passenger_name = input("Enter new passenger name >>> ").strip()
    if new_passenger_name == '':
        print("pasenger name maintained")

    new_flight_id=input("Enter new flight id name >>> ").strip()
    if new_flight_id == '':
        print(" flight id maintained")

    # Prepare the new ticket data
    new_ticket_data = {
        "passenger_name": new_passenger_name if new_passenger_name else tickets["passenger_name"],
        "flight id ": new_flight_id if new_flight_id else tickets["flight_id"],
        "updated_at": datetime.datetime.now()
    }

    # Update the terminal record in the database
    update_record(table=TICKET_TABLE_NAME, record_id=ticket_id, data=new_ticket_data )
    time.sleep(DEFAULT_SLEEP_TIME)


    def display_ticket_menu()->None:
      """Displays the gate management menu."""
    from utils.utils import display_menu

    sub_menu_title = f""
    sub_options = [
        "Display ticket",
        "Add ticket",
        "Update ticket",
        "Back",
    ]

    while True:
        # Display gate management menu
        display_menu(menu_title=sub_menu_title, options=sub_options)

        # Ask for user input
        user_action = int(input(f"Enter your choice (1-{len(sub_options)}) >>> ").strip())

        if user_action == 1:
            display_ticket_records(ticket_id['id'])
        elif user_action == 2:
            add_ticket_record(ticket_id['id'])
        elif user_action == 3:
            update_ticket_record(ticket_id['id'])
        elif user_action == 4:
            break
        else:
            print(f"Invalid choice! Please enter a number between 1 and {len(sub_options)}.")
            time.sleep(DEFAULT_SLEEP_TIME)


