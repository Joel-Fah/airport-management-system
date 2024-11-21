from utils.constants import DEFAULT_SLEEP_TIME
from utils.db_utils import update_record, fetch_records
from utils.utils import display_menu
from utils.utils import clear_screen
import time

message="Welcome to the flight service board "

clear_screen()

def collect():
    collected_info = {}
    
    collected_info['flight_number'] = input("Enter the flight number: ")
    collected_info['origin'] = input("Enter your origin: ")
    collected_info['destination'] = input("Enter the destination: ")
    collected_info['departure time'] = input("Enter the departure time: ")
    collected_info['arrival_time'] = input("Enter the arrival time: ")
    collected_info['aircraft_id'] = input("Enter the aircraft_id: ")
    collected_info['ailine_id'] = input("Enter the air line id: ")
    
    return collected_info






def adding_flight():     
       """Updates a flight list
     
     Args: flights info

     returns: A message if the update was succesfull
   
   """ 
       info=collect
       from utils.db_utils import insert_record
       insert_record("Flight",info)
  


def  Crew_info():
       """functions which checks if a specific crew memeber or passenger is or was found a flight  
     
        Args: dictcionary(dct) with flight_id  and  passenger/crew member  full name  as key value pair

       returns: A boolean True if the passenger was found or false it was not found"""
      

      # not easy to implement requires qn eloborqte select statement and some complicated outter joins and i need to sleep
       


def list_of_all_flights():
      """ creates a list of all the flights in that company
     
     Args: none

     returns: returns a dictionary with flight info
   

        """
      from utils.db_utils import print_all_records
      print_all_records("Flight")







 
def flight_service_menu():
    menu_title =" services_menu"

    options=[
        "Adding flight to the flight list"
        "Checking if a passenger or a pefersonel is on a specific flight"
        #flight status include Boarding, departed , in Air ,Delayed, Arrived,Gate closed , gate closed
        " listing all the flights "
        "Exit"
    ]
    while True:
        clear_screen()

        # Display main menu
        display_menu(menu_title, options)

        user_action = int(input(f"Select an option (1-{len(options)}) >>> ").strip())

        if user_action == 1:
            # Handle Option 1
            adding_flight()
        elif user_action == 2:
            Crew_info()
        elif user_action == 3:
               list_of_all_flights()
        
        elif user_action==4:
          print("loging out.....")
        elif user_action==5:
           
            break
        else:
            print(f"Invalid choice. Please enter a number between 1 and {len(options)}.")
            time.sleep(DEFAULT_SLEEP_TIME)

