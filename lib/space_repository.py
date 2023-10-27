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
            item = Space(row['id'], row['name'], row['description'], row['price'], row['owner_id'])
            spaces.append(item)
        return spaces
    
    def create(self, space):
        space_id = self._connection.execute("INSERT INTO spaces (name, description, price) VALUES (%s, %s, %s, %s) RETURNING id", [space.name, space.description, space.price, space.owner_id])
        return space_id['id']

    def find_by_space_name(self, space_name):
        row = self._connection.execute("SELECT * from spaces WHERE name = %s", [space_name])
        space = Space(row[0]['id'], row[0]['name'], row[0]['description'], row[0]['price'],row['owner_id'])
        return space
    
    def find_by_space_id(self, space_id):
        row = self._connection.execute("SELECT * from spaces WHERE id = %s", [space_id])
        space = Space(row[0]['id'], row[0]['name'], row[0]['description'], row[0]['price'], row[0]['owner_id'])
        return space
    
    

