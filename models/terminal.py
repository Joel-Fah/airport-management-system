class Terminal:
    def __init__(self, id, name, airport_id):
        self.id = id
        self.name = name
        self.airport_id = airport_id
        
    def __repr__(self):
        return f"Terminal(id={self.id}, name={self.name}, airport_id={self.airport_id})"
