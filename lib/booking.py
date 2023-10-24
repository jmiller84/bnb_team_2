class Booking:

    def __init__(self, id, user_id, space_id, date):
        self.id = id
        self.user_id = user_id
        self.space_id = space_id
        self.date = date

    def __repr__(self):
        return f"Booking(id: {self.id}, user_id: {self.user_id}, space_id: {self.space_id}, date: {self.date})"
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__