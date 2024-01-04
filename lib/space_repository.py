"""
Create
Read All
Update X
Delete X
Read 1
"""
from lib.space import Space

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM spaces")
        spaces = []
        for row in rows:
            item = Space(row['id'], row['name'], row['area'], row['country'], row['description'], row['price'], row['host_id'], row['image_url'], row['max_guests'])
            spaces.append(item)
        return spaces
    
    def create(self, space):
        space_id = self._connection.execute("INSERT INTO spaces (name, area, country, description, price, host_id, image_url, max_guests) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id", [space.name, space.area, space.country, space.description, space.price, space.host_id, space.image_url, space.max_guests])
        return space_id[0]['id']

    def find_by_space_name(self, space_name):
        row = self._connection.execute("SELECT * from spaces WHERE name = %s", [space_name])
        space = Space(row[0]['id'], row[0]['name'], row[0]['area'], row[0]['country'], row[0]['description'], row[0]['price'], row[0]['host_id'], row[0]['image_url'], row[0]['max_guests'])
        return space
    
    def find_by_space_id(self, space_id):
        row = self._connection.execute("SELECT * from spaces WHERE id = %s", [space_id])
        space = Space(row[0]['id'], row[0]['name'], row[0]['area'], row[0]['country'], row[0]['description'], row[0]['price'], row[0]['host_id'], row[0]['image_url'], row[0]['max_guests'])
        return space
    
    

