class Airport:
    def __init__(self, id, name, location, code):
        self.id = id
        self.name = name
        self.location = location
        self.code = code
        
    def __repr__(self):
        return f"Airport(id={self.id}, name={self.name}, location={self.location}, code={self.code})"
