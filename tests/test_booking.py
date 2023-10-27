from lib.booking import Booking

def test_booking_contstructs():
    booking = Booking(1, 1, 1, "2023-09-30")
    assert booking.id == 1
    assert booking.user_id == 1
    assert booking.space_id == 1
    assert booking.date == "2023-09-30"
    assert booking.confirmed == False

def test_booking_looks_nice():
    booking = Booking(1, 1, 1, "2023-09-30")
    assert str(booking) == "Booking(id: 1, user_id: 1, space_id: 1, date: 2023-09-30, confirmed: False)"

def test_two_bookings_with_same_attributes_are_equal():
    booking1 = Booking(1, 1, 1, "2023-09-30")
    booking2 = Booking(1, 1, 1, "2023-09-30")
    assert booking1 == booking2
    
def test_booking_with_confirmed_true_constructs_properly():
    booking = Booking(1, 1, 1, "2023-09-30", True)
    assert booking.id == 1
    assert booking.user_id == 1
    assert booking.space_id == 1
    assert booking.date == "2023-09-30"
    assert booking.confirmed == True