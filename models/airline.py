class Airline:
    def __init__(self, id, name, code, created_at, updated_at):
        self.id = id
        self.name = name
        self.code = code
        self.created_at = created_at
        self.updated_at = updated_at
        
    def __repr__(self):
        return f"Airline(id={self.id}, name={self.name}, code={self.code}), created_at={self.created_at}, updated_at={self.updated_at}"
