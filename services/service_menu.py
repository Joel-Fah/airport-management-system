import os
import time
from utils.constants import DEFAULT_SLEEP_TIME
import flight_service
import passenger_service
import airport_service
import terminal_service
import  gate_service
from utils.utils import display_menu
from utils.utils import clear_screen



#creating the entry point to the user services boards
# creating a menu so user can acess the diffrent services from the main menu
def services_main_menu():
    menu_title =" services_menu"

    options=[
        "Flight service"
        "Passenger service"
        "gate services"
        "airport services"
        "terminal services"
    ]
    while True:
        clear_screen()

        # Display main menu
        display_menu(menu_title, options)

        user_action = int(input(f"Select an option (1-{len(options)}) >>> ").strip())

        if user_action == 1:
            # Handle Option 1
            flight_service.display_menu_flight
        elif user_action == 2:
            passenger_service
        elif user_action == 3:
            gate_service.display_menu_gate
        elif user_action==4:
            airport_service.display_menu_airport
        elif user_action==5:
            terminal_service.display_menu_terminal
        elif user_action==6:
            print("loging out.....")
            break
        else:
            print(f"Invalid choice. Please enter a number between 1 and {len(options)}.")
            time.sleep(DEFAULT_SLEEP_TIME)

