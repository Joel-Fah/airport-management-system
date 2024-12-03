# db_utils.py

import sqlite3

# Database connection utilities
def connect_to_db(db_path="data/database.sqlite3"):
    """
    Establishes a connection to the SQLite3 database.
    
    Args:
        db_path (str): Path to the database file.
        
    Returns:
        connection (SQLite3): SQLite3 connection object
    """
    try:
        connection = sqlite3.connect(db_path)
        print(f"Connected to database at {db_path}")
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def close_connection(connection):
    """
    Closes the connection to the SQLite3 database.

    Args:
        connection (SQLite3): SQLite3 connection object
    """
    try:
        if connection:
            connection.close()
            print("Database connection closed.")
    except sqlite3.Error as e:
        print(f"Error closing the database connection: {e}")


# Basic CRUD operations
# Initialization and schema setup
def create_tables():
    """
    Creates the necessary tables for the system in the database.
    Includes all entities: Airport, Terminal, Gate, Flight, Passenger, Ticket, Staff.
    """
    
    tables = {
        "User": """
            CREATE TABLE IF NOT EXISTS User (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL,
                last_login DATETIME,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        """,
        "Airport": """
            CREATE TABLE IF NOT EXISTS Airport (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                location TEXT NOT NULL,
                code TEXT UNIQUE NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        """,
        "Terminal": """
            CREATE TABLE IF NOT EXISTS Terminal (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                airport_id INTEGER NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (airport_id) REFERENCES Airport(id)
            );
        """,
        "Gate": """
            CREATE TABLE IF NOT EXISTS Gate (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                gate_number TEXT NOT NULL,
                terminal_id INTEGER NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (terminal_id) REFERENCES Terminal(id)
            );
        """,
        "Flight": """
            CREATE TABLE IF NOT EXISTS Flight (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                flight_number TEXT UNIQUE NOT NULL,
                origin TEXT NOT NULL,
                destination TEXT NOT NULL,
                departure_time TEXT NOT NULL,
                arrival_time TEXT NOT NULL,
                gate_id INTEGER UNIQUE,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (gate_id) REFERENCES Gate(id)
            );
        """,
        "Passenger": """
            CREATE TABLE IF NOT EXISTS Passenger (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                passport_number TEXT UNIQUE NOT NULL,
                nationality TEXT NOT NULL,
                flight_id INTEGER NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES User(id),
                FOREIGN KEY (flight_id) REFERENCES Flight(id)
            );
        """,
        "Ticket": """
            CREATE TABLE IF NOT EXISTS Ticket (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ticket_number TEXT UNIQUE NOT NULL,
                passenger_id INTEGER NOT NULL,
                flight_id INTEGER NOT NULL,
                seat_number TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (passenger_id) REFERENCES Passenger(id),
                FOREIGN KEY (flight_id) REFERENCES Flight(id)
            );
        """,
        "Staff": """
            CREATE TABLE IF NOT EXISTS Staff (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                role TEXT NOT NULL,
                terminal_id INTEGER,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (terminal_id) REFERENCES Terminal(id)
            );
        """,
    }

    # Connect to the database
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            # Create each table
            for table_name, create_query in tables.items():
                print(f"Creating table: {table_name}")
                cursor.execute(create_query)
            connection.commit()
            print("All tables created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")
        finally:
            close_connection(connection)


# Basic CRUD operations

def insert_record(table, data):
    """
    Inserts a record into a specified table.
    
    Args:
        table (str): Name of the table
        data (dict): Dictionary of column names and their corresponding values.
    
    Returns:
        ID (int): The ID of the inserted record or None if an error occurs.
    """
    
    # Connect to the database
    connection = connect_to_db()
    if not connection:
        return None

    try:
        # Prepare the columns and placeholders for the SQL query
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?" for _ in data.values()])
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

        # Execute the query
        cursor = connection.cursor()
        cursor.execute(query, tuple(data.values()))
        connection.commit()

        # Return the ID of the inserted record
        print(f"Record inserted into {table} with ID: {cursor.lastrowid}")
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Error inserting record into {table}: {e}")
        return None
    finally:
        close_connection(connection)



def update_record(table, record_id, new_data):
    """
    Updates a record in a specified table by its ID.
    
    Args:
        table (str): Name of the table.
        record_id (int): The ID of the record to update.
        new_data (dict): Dictionnary of column names and their corresponding new values.
        
    Returns:
        status (bool): True if the update was successful, False otherwise.
    """
    connection = connect_to_db()
    if not connection:
        return False

    try:
        # Prepare the SET part of the SQL query
        set_clause = ", ".join([f"{column} = ?" for column in new_data.keys()])
        query = f"UPDATE {table} SET {set_clause} WHERE id = ?"

        # Execute the query
        cursor = connection.cursor()
        cursor.execute(query, tuple(new_data.values()) + (record_id,))
        connection.commit()

        # Check if any rows were affected
        if cursor.rowcount > 0:
            print(f"Record with ID {record_id} in {table} updated successfully.")
            return True
        else:
            print(f"No record with ID {record_id} found in {table}.")
            return False
    except sqlite3.Error as e:
        print(f"Error updating record in {table}: {e}")
        return False
    finally:
        close_connection(connection)



def delete_record(table, record_id):
    """
    Deletes a record from a specified table by its ID.
    
    Args:
        table (str): Name of the table.
        record_id (int): The ID of the record to delete.
        
    Returns:
        status (bool): True if the deletion was successful, False otherwise.
    """
    
    connection = connect_to_db()
    if not connection:
        return False

    try:
        # Prepare the SQL query
        query = f"DELETE FROM {table} WHERE id = ?"

        # Execute the query
        cursor = connection.cursor()
        cursor.execute(query, (record_id,))
        connection.commit()

        # Check if any rows were affected
        if cursor.rowcount > 0:
            print(f"Record with ID {record_id} deleted from {table}.")
            return True
        else:
            print(f"No record with ID {record_id} found in {table}.")
            return False
    except sqlite3.Error as e:
        print(f"Error deleting record from {table}: {e}")
        return False
    finally:
        close_connection(connection)


def fetch_records(table, filters=None, fields="*") -> list:
    """
    Fetches records from a specified table, optionally filtering by specific criteria and selecting specific fields.

    Args:
        table (str): Name of the table to fetch data from.
        filters (dict): Dictionary of column-value pairs to filter the records (optional).
        fields (str): Comma-separated string of fields to select (default is '*').

    Returns:
        records (list): A list of dictionaries representing the fetched records, or an empty list if none found.
    """
    connection = connect_to_db()
    if not connection:
        return []

    try:
        # Base query to select specified fields
        query = f"SELECT {fields} FROM {table}"
        parameters = ()

        # Add WHERE clause if filters are provided
        if filters:
            filter_clause = " AND ".join([f"{column} = ?" for column in filters.keys()])
            query += f" WHERE {filter_clause}"
            parameters = tuple(filters.values())

        # Execute the query
        cursor = connection.cursor()
        cursor.execute(query, parameters)

        # Fetch all rows
        rows = cursor.fetchall()

        # Retrieve column names to build dictionaries
        column_names = [description[0] for description in cursor.description]

        # Convert rows to list of dictionaries
        records = [dict(zip(column_names, row)) for row in rows]

        return records
    except sqlite3.Error as e:
        print(f"Error fetching records from {table}: {e}")
        return []
    finally:
        close_connection(connection)


# Utility for debugging
# db_utils.py

def print_all_records(table):
    """
    Fetches and prints all records from a specified table in a readable format.
    
    Args:
        table (str): Name of the table to fetch data from.
    """
    
    connection = connect_to_db()
    if not connection:
        print("Failed to connect to the database.")
        return

    try:
        # Prepare the query to fetch all records
        query = f"SELECT * FROM {table}"

        # Execute the query
        cursor = connection.cursor()
        cursor.execute(query)

        # Fetch all rows
        rows = cursor.fetchall()

        # Retrieve column names to display as headers
        column_names = [description[0] for description in cursor.description]

        # Print the header
        print(f"Records from table '{table}':")
        print("-" * 50)
        print(" | ".join(column_names))
        print("-" * 50)

        # Print each record row by row
        for row in rows:
            print(" | ".join(map(str, row)))

        if not rows:
            print("No records found.")

    except sqlite3.Error as e:
        print(f"Error fetching records from {table}: {e}")
    finally:
        close_connection(connection)

def join_tables_and_selected_fields():
    """
    Fetches and join database tables with specific fields.
    """
    
    connection = connect_to_db()
    if not connection:
        print("Failed to connect to the database.")
        return
    
    try:
        # promt the user input
      table1 = input("Enter the first table name (e.g., flights): ") 
      table2 = input("Enter the second table name (e.g., passengers): ") 
      join_field = input(f"Enter the field to join on (e.g., flight_number): ")
      fields_table1 = input(f"Enter the fields to select from {table1} (comma-separated): ").split(',') 
      fields_table2 = input(f"Enter the fields to select from {table2} (comma-separated): ").split(',') 
      # Clean up field names and construct the select clause 
      fields_table1 = [field.strip() for field in fields_table1]
      fields_table2 = [field.strip() for field in fields_table2]
      select_fields = ', '.join([f"{table1}.{field}" for field in fields_table1] + [f"{table2}.{field}" for field in fields_table2]) 
      query = f''' SELECT {select_fields} FROM {table1} JOIN {table2} ON {table1}.{join_field} = {table2}.{join_field} '''
       # Execute the query
      cursor = connection.cursor()
      cursor.execute(query)
      rows= cursor.fetchall()
      connection.commit()

      # Create a list of dictionaries from the result 
      result = [] 
      columns = fields_table1 + fields_table2
      for row in rows: 
        row_dict = dict(zip(columns, row))
        result.append(row_dict) 
        return result

    finally:
        close_connection(connection)

