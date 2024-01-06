from lib.booking import Booking


class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM bookings")
        bookings = [Booking(row['id'], row['user_id'], row['space_id'], row['date'], row['confirmed']) for row in rows]
        return bookings
    
    def create(self, booking):
        self._connection.execute("INSERT INTO bookings (user_id, space_id, date, confirmed) VALUES (%s, %s, %s, False)", [booking.user_id, booking.space_id, booking.date])
    
    def find_by_user_id(self, user_id):
        rows = self._connection.execute("SELECT * FROM BOOKINGS WHERE user_id = %s", [user_id])
        bookings = [Booking(row['id'], row['user_id'], row['space_id'], row['date'], row['confirmed']) for row in rows]
        return bookings
    
    def find_by_space_id(self, space_id):
        rows = self._connection.execute("SELECT * FROM BOOKINGS WHERE space_id = %s", [space_id])
        bookings = [Booking(row['id'], row['user_id'], row['space_id'], row['date'], row['confirmed']) for row in rows]
        return bookings

    def show_unavailable_dates_for_space(self, space_id):
        bookings = self.find_by_space_id(space_id)
        dates = [booking.date for booking in bookings]
        return dates
    
    def delete(self, booking_id):
        self._connection.execute("DELETE FROM bookings WHERE id = %s", [booking_id])

    def find_confirmed_bookings_by_user_id(self, user_id):
        rows = self._connection.execute("SELECT * FROM BOOKINGS WHERE confirmed = True and user_id = %s", [user_id])
        bookings = [Booking(row['id'], row['user_id'], row['space_id'], row['date'], row['confirmed']) for row in rows]
        return bookings
    
    def find_all_unconfirmed_booking_requests(self, user_id):

        sql_query = """
                SELECT
                    bookings.id as booking_id,
                    bookings.user_id,
                    bookings.space_id,
                    bookings.date,
                    bookings.confirmed,
                    spaces.name,
                    spaces.host_id
                FROM
                    bookings
                JOIN
                    spaces ON bookings.space_id = spaces.id
                WHERE spaces.host_id = %s 
                and confirmed = False 
                and spaces.host_id != bookings.user_id
                    """

        rows = self._connection.execute(sql_query, [user_id])
        return rows
    
    def update_booking_to_confirmed(self, booking_id):
        self._connection.execute("UPDATE bookings SET confirmed = True WHERE id = %s", [booking_id])
