class Passenger:
    def __init__(self, id, name, passport_number, nationality):
        self.id = id
        self.name = name
        self.passport_number = passport_number
        self.nationality = nationality
        
    def __repr__(self):
        return f"Passenger(id={self.id}, name={self.name}, passport_number={self.passport_number}, nationality={self.nationality})"
