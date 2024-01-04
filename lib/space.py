class Space:
    
    def __init__(self, id, name, area, country, description, price, host_id, image_url, max_guests):
        self.id = id 
        self.name = name
        self.area = area
        self.country = country
        self.description = description
        self.price = price
        self.host_id = host_id
        self.image_url = image_url
        self.max_guests = max_guests

    def __repr__(self):
        return f"Space({self.id}, {self.name}, {self.area}, {self.country}, {self.description}, {self.price}, {self.host_id}, {self.image_url}, {self.max_guests})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__