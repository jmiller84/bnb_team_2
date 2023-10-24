from lib.booking import Booking


class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM bookings")
        bookings = [Booking(row['id'], row['user_id'], row['space_id'], row['date']) for row in rows]
        return bookings