class User:
    def __init__(self, id, username, email, password, role, created_at, updated_at):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, email={self.email}, role={self.role}), created_at={self.created_at}, updated_at={self.updated_at}"
