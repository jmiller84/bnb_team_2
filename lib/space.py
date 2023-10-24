class Space:
    
    def __init__(self, id, name, description, price):
        self.id = id 
        self.name = name
        self.description = description
        self.price = price

    def __repr__(self):
        return f"Space({self.id}, {self.name}, {self.description}, {self.price})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__