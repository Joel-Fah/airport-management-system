class Passenger:
    def __init__(self, id, name, passport_number, nationality, created_at, updated_at):
        self.id = id
        self.name = name
        self.passport_number = passport_number
        self.nationality = nationality
        self.created_at = created_at
        self.updated_at = updated_at
        
    def __repr__(self):
        return f"Passenger(id={self.id}, name={self.name}, passport_number={self.passport_number}, nationality={self.nationality}), created_at={self.created_at}, updated_at={self.updated_at}"
