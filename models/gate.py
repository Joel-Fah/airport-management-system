class Gate:
    def __init__(self, id, number, terminal_id, created_at, updated_at):
        self.id = id
        self.number = number
        self.terminal_id = terminal_id
        self.created_at = created_at
        self.updated_at = updated_at
        
    def __repr__(self):
        return f"Gate(id={self.id}, number={self.number}, terminal_id={self.terminal_id}), created_at={self.created_at}, updated_at={self.updated_at}"
