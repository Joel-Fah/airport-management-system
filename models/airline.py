class Airline:
    def __init__(self, id, name, code):
        self.id = id
        self.name = name
        self.code = code
        
    def __repr__(self):
        return f"Airline(id={self.id}, name={self.name}, code={self.code})"