class Ticket:
    def __init__(self, id, ticket_number, passenger_id, flight_id, seat_number):
        self.id = id
        self.ticket_number = ticket_number
        self.passenger_id = passenger_id
        self.flight_id = flight_id
        self.seat_number = seat_number
        
    def __repr__(self):
        return f"Ticket(id={self.id}, ticket_number={self.ticket_number}, passenger_id={self.passenger_id}, flight_id={self.flight_id}, seat_number={self.seat_number})"
