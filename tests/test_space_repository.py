from lib.space_repository import SpaceRepository
from lib.space import Space

"""
Tests:
    - when we read all spaces, we see a list of all spaces
    - when we create a new space, it is displayed in the list of all spaces
    - When we call find_space_by_title, we see the space displayed
    TODO:
    - when we update a space, we see the change in the list of all spaces X
    - when we delete a space X
"""

# when we read all spaces, we see a list of all spaces in database

def test_list_all_spaces(db_connection):
    db_connection.seed("seeds/MBnB.sql")
    repository = SpaceRepository(db_connection)
    assert repository.all() == [
        Space(1, 'Cottage', 'Wimborne', 'UK', 'A nice cottage', 27, 4, 'images/cottage.jpeg', 6),
        Space(2, 'Villa', 'Nice', 'France', 'A mediterranean villa with a sea view', 70, 2, 'images/mediterraneanVilla.jpeg', 5),
        Space(3, 'Alpine lodge', 'Brig-Glis', 'Switzerland', 'A cosy ski lodge with wood-burning fire', 95, 1, 'images/AlpineLodge.jpeg', 6),
        Space(4, 'Studio Apartment', 'New York', 'USA', 'A cool apartment in the centre of the bustling city', 102, 3, 'images/studioApartment.jpeg', 2),
        Space(5, 'Tent', 'Tenby', 'UK', 'A 5 metre, cotton canvas bell tent which can comfortably accommodate up to 4 people with any combination of single beds or double bed, duvets and pillows with linen, rugs, blankets, cushions, lighting, side tables, seating and plants.', 50, 2, 'images/tent.jpeg', 3)
    ]


# - when we create a new space, it is displayed in the list of all spaces
def test_create_a_new_space(db_connection):
    db_connection.seed("seeds/MBnB.sql")
    repository = SpaceRepository(db_connection)
    repository.create(Space(None, 'Cabin', 'Tampaksiring', 'Indonesia', 'Located just a 20-minute scooter ride from the vibrant centre of Ubud, the Dome is a newly built one bedroom bamboo cabin situated within the Eco Six Resort.', 230, 3, 'images/cabin.jpeg', 3))
    assert repository.all() == [
        Space(1, 'Cottage', 'Wimborne', 'UK', 'A nice cottage', 27, 4, 'images/cottage.jpeg', 6),
        Space(2, 'Villa', 'Nice', 'France', 'A mediterranean villa with a sea view', 70, 2, 'images/mediterraneanVilla.jpeg', 5),
        Space(3, 'Alpine lodge', 'Brig-Glis', 'Switzerland', 'A cosy ski lodge with wood-burning fire', 95, 1, 'images/AlpineLodge.jpeg', 6),
        Space(4, 'Studio Apartment', 'New York', 'USA', 'A cool apartment in the centre of the bustling city', 102, 3, 'images/studioApartment.jpeg', 2),
        Space(5, 'Tent', 'Tenby', 'UK', 'A 5 metre, cotton canvas bell tent which can comfortably accommodate up to 4 people with any combination of single beds or double bed, duvets and pillows with linen, rugs, blankets, cushions, lighting, side tables, seating and plants.', 50, 2, 'images/tent.jpeg', 3),
        Space(6, 'Cabin', 'Tampaksiring', 'Indonesia', 'Located just a 20-minute scooter ride from the vibrant centre of Ubud, the Dome is a newly built one bedroom bamboo cabin situated within the Eco Six Resort.', 230, 3, 'images/cabin.jpeg', 3)
    ]

# When we call find_space_by_title, we see the space displayed

def test_find_space_by_name_returns_single_space(db_connection):
    db_connection.seed("seeds/MBnB.sql")
    repository = SpaceRepository(db_connection)
    space = repository.find_by_space_name("Alpine lodge")
    assert space == Space(3, 'Alpine lodge', 'Brig-Glis', 'Switzerland', 'A cosy ski lodge with wood-burning fire', 95, 1, 'images/AlpineLodge.jpeg', 6)