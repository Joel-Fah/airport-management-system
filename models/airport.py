class Airport:
    def __init__(self, id, name, location, code, created_at, updated_at):
        self.id = id
        self.name = name
        self.location = location
        self.code = code
        self.created_at = created_at
        self.updated_at = updated_at
        
    def __repr__(self):
        return f"Airport(id={self.id}, name={self.name}, location={self.location}, code={self.code}), created_at={self.created_at}, updated_at={self.updated_at}"
