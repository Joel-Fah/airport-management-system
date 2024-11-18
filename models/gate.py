class Gate:
    def __init__(self, id, number, terminal_id):
        self.id = id
        self.number = number
        self.terminal_id = terminal_id
        
    def __repr__(self):
        return f"Gate(id={self.id}, number={self.number}, terminal_id={self.terminal_id})"