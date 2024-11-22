class Terminal:
    def __init__(self, id, name, airport_id, created_at, updated_at):
        self.id = id
        self.name = name
        self.airport_id = airport_id
        self.created_at = created_at
        self.updated_at = updated_at
        
    def __repr__(self):
        return f"Terminal(id={self.id}, name={self.name}, airport_id={self.airport_id}), created_at={self.created_at}, updated_at={self.updated_at}"
