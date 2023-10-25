from lib.user import User
"""
list users
create user
find user by id
"""

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM users")
        users = [User(row['id'], row['username'], row['password']) for row in rows]
        return users
    
    def create(self, new_user):
        self._connection.execute("INSERT INTO users (username, password) VALUES (%s, %s)", [new_user.username, new_user.password])

    def find_user_by_user_id(self, user_id):
        row = self._connection.execute("SELECT * FROM users WHERE id = %s", [user_id])
        user = User(row[0]['id'], row[0]['username'], row[0]['password'])
        return user