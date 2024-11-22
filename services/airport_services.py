from utils.constants import DEFAULT_SLEEP_TIME
from utils.db_utils import update_record, fetch_records
from utils.utils import display_menu
from utils.utils import clear_screen

import time

message="Welcome to the airport mangement board "

clear_screen()






def add_airport():
      """
    Inserts a record into a specified  airport table.
    
    Args:
        airport_data (dict): Dictionary of column names and their corresponding values.
    
    Returns:
        ID (int): The ID of the inserted record or None if an error occurs.
    """
      
      
      airport_name= input("Enter airport name >>>>").strip,
      airport_location=  input("Enter airport location >>>>").strip,
      airport_code=  input("Enter airport code >>>>").strip,
    
      
      airport_data = {
           "airport_name": airport_name, 
            "airport_location": airport_location,
            "airport_code": airport_code 
            }
      from utils.db_utils import insert_record

      insert_record("Airport",airport_data)

      
       
       
       
    
     






def  display_airports():
     """
    Displays all the users in the database.
    """
     from utils.utils import display_records

     table = "Airport"
     fields = "id, name, location, code"

     all_aiports = fetch_records(table, fields=fields)
     display_records(all_aiports)
      


def update_airport(airport_data):
   """
    Updates the user record in the database with the new details provided by the user.

    Args:
        airport_data (dict): aiport details to update.

    Returns:
        bool: True if the user record was updated successfully, else False.
    """
   from utils.utils import clear_screen, display_menu_title

    # Clear the screen before showing the menu
   clear_screen()                 
    

    # Display the user details
   display_menu_title("Edit  Airport info ")
   print("Current Airports details:")
   print(f"airport_name: {airport_data['airport_name']}")
   print(f"airport_location: {airport_data['airport_location']}")
   print(f"airport_code: {airport_data['airport_code']}")
   print(f"airport_id: {airport_data['airport_id']}", end="\n\n")

    # Ask for new details
   new_airportname = input("Enter new airport code (leave blank to keep current) >>> ").strip()
    
   if new_airportname == '':
    print("Airport name maintained")
           

   new_airportlocation = input("Enter new location (leave blank to keep current) >>> ").strip()
    
    
   if new_airportlocation == '':
       print("Airport location maintained")
    
   new_airportcode = input("Enter new airport code (leave blank to keep current) >>> ").strip()
    
   if new_airportcode == '':
    print("Airport code maintained")

    new_data = {
        "aiport_name": new_airportname if new_airportname else airport_data["aiport_name"],
        "aiport_location": new_airportlocation if new_airportlocation else airport_data["aiport_location"],
        "aiport_code": new_airportcode if new_airportcode else airport_data["aiport_code"],
    }
    clear_screen()
   update_record("Airport", airport_data["id"], new_data)
   print("updating airport info.......")
   clear_screen()





def delete_airport(airport_id):
   """
    Deletes the airport record from the database.

    Args:
        user_id (int): The ID of the Airport to delete. 

    Returns:
        bool: True if the user record was deleted successfully, else False.
    """
   from utils.db_utils import delete_record

    # Delete the user record from the database
   return delete_record("Airport", airport_id)









 
def airport_service_menu():
    menu_title =" services_menu"

    options=[
        "Add new airport"
        ""
        "Display all the airports"

        "update Airport info"

        "Delete an airport " 
        
         " Exit"




    ]
    while True:
        clear_screen()

        # Display main menu
        display_menu(menu_title, options)

        user_action = int(input(f"Select an option (1-{len(options)}) >>> ").strip())

        if user_action == 1:
            # Handle Option 1
            add_airport()
        elif user_action == 2:
            display_airports()
        elif user_action == 3:
               update_airport()
        elif user_action == 4:
               delete_airport()
        elif user_action==5:
          print("loging out.....")
        elif user_action==6:
           
            break
        else:
            print(f"Invalid choice. Please enter a number between 1 and {len(options)}.")
            time.sleep(DEFAULT_SLEEP_TIME)

