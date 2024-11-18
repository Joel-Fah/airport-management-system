class Staff:
    def __init__(self, id, name, role, terminal_id=None):
        self.id = id
        self.name = name
        self.role = role
        self.terminal_id = terminal_id
        
    def __repr__(self):
        return f"Staff(id={self.id}, name={self.name}, role={self.role}, terminal_id={self.terminal_id})"