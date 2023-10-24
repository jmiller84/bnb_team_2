from lib.booking_repository import BookingRepository
from lib.booking import Booking
from datetime import date

def test_all_method_shows_all_bookings(db_connection):
    db_connection.seed("seeds/MBnB.sql")
    repository = BookingRepository(db_connection)
    assert repository.all() == [
        Booking(1, 1, 1, date(2023,10,30)),
        Booking(2, 2, 1, date(2023,9,25)),
        Booking(3, 2, 3, date(2023,10,10)),
        Booking(4, 3, 1, date(2023,9,6)),
        Booking(5, 1, 2, date(2023,10,7)),
        Booking(6, 4, 2, date(2023,9,15))
    ]