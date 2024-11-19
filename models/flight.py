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
        
    def __repr__(self):
        return f"Flight(id={self.id}, flight_number={self.flight_number}, origin={self.origin}, destination={self.destination}, departure_time={self.departure_time}, arrival_time={self.arrival_time}, aircraft_id={self.aircraft_id}, airline_id={self.airline_id})"
