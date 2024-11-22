from utils.constants import DEFAULT_SLEEP_TIME
from utils.db_utils import update_record, fetch_records
from utils.utils import display_menu
from utils.utils import clear_screen

import time

message="Welcome to the airport mangement board "

clear_screen()






def staff_mangement():     
       """allocates staff to thier diffrent missions
     
     Args: 

     returns: 
   
   """ 


def  resouece_alloction():
       """functions which allocates the necssary resources to the diffrent opertions(flight)
       such as aircraft , gates number an terminal  
     
        Args: flight_id ,gate id

       returns: A boolean"""
      

      


def Anoucements():
      """ creates anouncements on the diifrent updates such as delayed flight and security issues 
     
     Args: none

     returns: returns a dictionary with flight info
   

        """
      from utils.db_utils import print_all_records
      print_all_records("Flight")







 
def airport_service_menu():
    menu_title =" services_menu"

    options=[
        "Staff mangement"
        ""
        "Resource allocation"

        "Anoucements "


    ]
    while True:
        clear_screen()

        # Display main menu
        display_menu(menu_title, options)

        user_action = int(input(f"Select an option (1-{len(options)}) >>> ").strip())

        if user_action == 1:
            # Handle Option 1
            staff_mangement()
        elif user_action == 2:
            resouece_alloction()
        elif user_action == 3:
               Anoucements()
        
        elif user_action==4:
          print("loging out.....")
        elif user_action==5:
           
            break
        else:
            print(f"Invalid choice. Please enter a number between 1 and {len(options)}.")
            time.sleep(DEFAULT_SLEEP_TIME)

