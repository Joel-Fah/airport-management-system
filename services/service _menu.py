import os
import time
from utils.constants import DEFAULT_SLEEP_TIME
import flight_service
import passenger_service
import reporting_service
import  user_service
from utils.utils import display_menu
from utils.utils import clear_screen



#creating the entry point to the user services boards
# creating a menu so user can acess the diffrent services from the main menu
def services_main_menu():
    menu_title =" services_menu"

    options=[
        "Flight service"
        "Passenger service"
        "Reporting service"
        "user service"
    ]
    while True:
        clear_screen()

        # Display main menu
        display_menu(menu_title, options)

        user_action = int(input(f"Select an option (1-{len(options)}) >>> ").strip())

        if user_action == 1:
            # Handle Option 1
            pass
        elif user_action == 2:
            pass
        elif user_action == 3:
            pass
        elif user_action==4:
            pass
        elif user_action==5:
            print("loging out.....")
            break
        else:
            print(f"Invalid choice. Please enter a number between 1 and {len(options)}.")
            time.sleep(DEFAULT_SLEEP_TIME)

