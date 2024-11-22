class Aircraft:
    def __init__(self, id, model, capacity, airline_id, created_at, updated_at):
        self.id = id
        self.model = model
        self.capacity = capacity
        self.airline_id = airline_id
        self.created_at = created_at
        self.updated_at = updated_at
        
    def __repr__(self):
        return f"Aircraft(id={self.id}, model={self.model}, capacity={self.capacity}, airline_id={self.airline_id}), created_at={self.created_at}, updated_at={self.updated_at}"
