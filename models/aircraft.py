class Aircraft:
    def __init__(self, id, model, capacity, airline_id):
        self.id = id
        self.model = model
        self.capacity = capacity
        self.airline_id = airline_id
        
    def __repr__(self):
        return f"Aircraft(id={self.id}, model={self.model}, capacity={self.capacity}, airline_id={self.airline_id})"