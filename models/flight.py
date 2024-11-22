class Flight:
    def __init__(self, id, flight_number, origin, destination, departure_time, arrival_time, price, aircraft_id, airline_id,
                 created_at, updated_at):
        self.id = id
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price = price
        self.aircraft_id = aircraft_id
        self.airline_id = airline_id
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"Flight(id={self.id}, flight_number={self.flight_number}, origin={self.origin}, destination={self.destination}, departure_time={self.departure_time}, arrival_time={self.arrival_time}, aircraft_id={self.aircraft_id}, airline_id={self.airline_id}), created_at={self.created_at}, updated_at={self.updated_at}"
