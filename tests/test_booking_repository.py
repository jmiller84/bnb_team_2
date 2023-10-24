from lib.booking_repository import BookingRepository
from lib.booking import Booking
from datetime import date


"""
When we call the all method we see a list of all booking objects
"""
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

"""
When we create a new booking we see the booking listed in the list of bookings
"""
def test_create_new_booking(db_connection):
    db_connection.seed("seeds/MBnB.sql")
    repository = BookingRepository(db_connection)
    new_booking = Booking(None, 1, 3, date(2023,10,27))
    repository.create(new_booking)
    assert repository.all() == [
        Booking(1, 1, 1, date(2023,10,30)),
        Booking(2, 2, 1, date(2023,9,25)),
        Booking(3, 2, 3, date(2023,10,10)),
        Booking(4, 3, 1, date(2023,9,6)),
        Booking(5, 1, 2, date(2023,10,7)),
        Booking(6, 4, 2, date(2023,9,15)),
        Booking(7, 1, 3, date(2023,10,27))
    ]

"""
When we find by user_id it returns a list of all bookings made by that user
"""
def test_find_by_user_id(db_connection):
    db_connection.seed("seeds/MBnB.sql")
    repository = BookingRepository(db_connection)
    user_bookings = repository.find_by_user_id(2)
    assert user_bookings == [
        Booking(2, 2, 1, date(2023,9,25)),
        Booking(3, 2, 3, date(2023,10,10))
    ]

"""
When we find by space_id it returns a list of all bookings for that space
"""
def test_find_by_space_id(db_connection):
    db_connection.seed("seeds/MBnB.sql")
    repository = BookingRepository(db_connection)
    space_bookings = repository.find_by_space_id(2)
    assert space_bookings == [
        Booking(5, 1, 2, date(2023,10,7)),
        Booking(6, 4, 2, date(2023,9,15))
    ]

"""
When we call list unavailable dates for a space, it returns a list of dates
"""
def test_list_unavailable_dates_for_space(db_connection):
    db_connection.seed("seeds/MBnB.sql")
    repository = BookingRepository(db_connection)
    unavailable_dates = repository.show_unavailable_dates_for_space(1)
    assert unavailable_dates == [date(2023,10,30), date(2023,9,25), date(2023,9,6)]

"""
when we call delete, it deletes a booking by booking id
"""
def test_delete_by_booking_id(db_connection):
    db_connection.seed("seeds/MBnB.sql")
    repository = BookingRepository(db_connection)
    repository.delete(4)
    assert repository.all() == [
        Booking(1, 1, 1, date(2023,10,30)),
        Booking(2, 2, 1, date(2023,9,25)),
        Booking(3, 2, 3, date(2023,10,10)),
        Booking(5, 1, 2, date(2023,10,7)),
        Booking(6, 4, 2, date(2023,9,15)),
    ]
    
