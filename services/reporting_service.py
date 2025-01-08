import datetime
import time

from utils.constants import DEFAULT_SLEEP_TIME
from utils.db_utils import update_record, fetch_records,insert_record


REPORT_TABLE_NAME = "Reports"
REPORT_DISPLAY_FIELDS = "Id, flight_id, passenger_id, report_content"

# function to summit complain


def add_Reort()-> None:
   print("please cearfully all neccesary details in case of lost/bagages article i.e color,bagage ticket number ")
   """Adds a new flight to the database."""
   from utils.db_utils import insert_record

    # Ask for report details
   passenger_id = input("Enter the passenger id >>> ").strip()
   flight_id = input("Enter flight id >>> ").strip()
   report_content= input("Enter report content   >>> ")
    

    # Prepare the report data
   Report_data = {
        
        "flight_id": flight_id,
        "passenger_id": passenger_id,
        "content":report_content,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now()
    }

    # Insert the Report record into the database
   insert_record(table=REPORT_TABLE_NAME, data=Report_data)
   time.sleep(DEFAULT_SLEEP_TIME)


def dislay_report(passenger_id:int,flight_id:int):
    from utils.db_utils import fetch_records
    from utils.utils import display_records
    
    reports=fetch_records(table=REPORT_TABLE_NAME,fields=REPORT_DISPLAY_FIELDS,filters={"passenger_id":passenger_id,"flight_id":flight_id,})
    display_records(reports)
    time.sleep(DEFAULT_SLEEP_TIME)



def delete_report(passenger_id:int,flight_id:int):
    """Deletes a report record from the database."""
    from utils.db_utils import delete_record, fetch_records
    from utils.utils import display_records

    # Fetch all reports from the database
    report = fetch_records(table=REPORT_TABLE_NAME, fields=REPORT_DISPLAY_FIELDS, filters={"passenger_id": passenger_id,"flight_id":flight_id,})

    # Display the reports
    display_records(records=report)

    # Ask for the report ID to delete
    report_id = int(input("Enter the ID of the report to delete >>> ").strip())

    # Delete the report record from the database
    delete_record(table=REPORT_TABLE_NAME, record_id=report_id)
    time.sleep(DEFAULT_SLEEP_TIME)

def update_report(passenger_id:int,flight_id:int):
    from utils.db_utils import delete_record, fetch_records
    from utils.utils import display_records



    # Fetch the report record from the database
    report = fetch_records(table=REPORT_TABLE_NAME, filters={"id": passenger_id, "id":flight_id,})[0]
        
    # Display the reports
    display_records(records=report)
    
    report_id = int(input("Enter the ID of the report to delete >>> ").strip())
    # Ask for the new report details
    passengers_id = input(
        f"Enter new passenger id (leave blank to keep current: {report['pasenger_id']}) >>> ").strip()
    flights_id = input(f"Enter new departure location (leave blank to keep current: {report['flight_id']}) >>> ").strip()
    report_content= input(
        f"Enter new destination location (leave blank to keep current: {report['report_content']}) >>> ").strip()
   
    

    # Prepare the new report data
    new_data = {
        "passengers_id": passenger_id if passengers_id else report["passenger_id"],
        "flight_id": flights_id if flights_id else report["report_id"],
        "content": report_content if report_content else report["report"],
        
       
        "updated_at": datetime.datetime.now()
    }

    # Update the report record in the database
    update_record(table=REPORT_TABLE_NAME, record_id=report_id, new_data=new_data)
    time.sleep(DEFAULT_SLEEP_TIME)

def display_menu_flight(report_record):
    """Displays the reports management menu."""
    from utils.utils import display_menu

    menu_title = f"Manage reports: Gate {report_record['repord_id']}"
    options = [
        "View reports",
        "Add a new report",
        "Edit a report",
        "Delete a report",
        "Back",
    ]

    while True:
        # display reports management menu
        print("\n")
        display_menu(menu_title=menu_title, options=options)

        # Ask for user input
        user_action = int(input(f"Enter your choice (1-{len(options)}) >>> ").strip())

        if user_action == 1:
            dislay_report(passenger_id=['id'],flight_id=["id"])
            close_input = input("Press enter to continue...")

            if close_input:
                continue
        elif user_action == 2:
            add_Reort()
        elif user_action == 3:
            update_report(passenger_id=['id'],flight_id=["id"])
        elif user_action == 4:
            delete_report(passenger_id=['id'],flight_id=["id"])
        elif user_action == 5:
            break
        else:
            print(f"Invalid choice! Please enter a number between 1 and {len(options)}.")
            time.sleep(DEFAULT_SLEEP_TIME)
