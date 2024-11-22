class Staff:
    def __init__(self, id, name, role, created_at, updated_at, terminal_id):
        self.id = id
        self.name = name
        self.role = role
        self.created_at = created_at
        self.updated_at = updated_at
        self.terminal_id = terminal_id

    def __repr__(self):
        return f"Staff(id={self.id}, name={self.name}, role={self.role}, terminal_id={self.terminal_id}), created_at={self.created_at}, updated_at={self.updated_at}"
