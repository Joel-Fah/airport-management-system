class Flight:
    def __init__(self, id, flight_number, origin, destination, departure_time, arrival_time, aircraft_id, airline_id):
        self.id = id
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.aircraft_id = aircraft_id
        self.airline_id = airline_id