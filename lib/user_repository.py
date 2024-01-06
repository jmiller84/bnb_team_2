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
        new_user_id = self._connection.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s) RETURNING id",
            [new_user.username, new_user.password])
        # Side effect: set the `id` of the User object passed as argument
        new_user.id = new_user_id[0]['id']

    def find_user_by_user_id(self, user_id):
        row = self._connection.execute("SELECT * FROM users WHERE id = %s", [user_id])
        user = User(row[0]['id'], row[0]['username'], row[0]['password'])
        return user
    
    def find_bookings_by_user_id_with_space_info_as_dictionary(self, user_id):
        sql_query = """
            SELECT
                users.id AS user_id,
                users.username,
                spaces.id AS space_id,
                spaces.name,
                spaces.description,
                spaces.price,
                spaces.host_id,
                bookings.id AS booking_id,
                bookings.date,
                bookings.confirmed
            FROM
                users
            JOIN
                bookings ON bookings.user_id = users.id
            JOIN spaces ON bookings.space_id = spaces.id
            WHERE users.id = %s AND spaces.host_id != user_id
        """
        results = self._connection.execute(sql_query, [user_id])
        return results
    