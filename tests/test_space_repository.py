from lib.space_repository import SpaceRepository
from lib.space import Space

"""
Tests:
    - when we create a new space, it is displayed in the list of all spaces
    - when we read all spaces, we see a list of all spaces
    - When we call find_space_by_title, we see the space displayed
    - when we update a space, we see the change in the list of all spaces X
    - when we delete a space X
"""
# - when we create a new space, it is displayed in the list of all spaces


def test_list_all_spaces(db_connection):
    db_connection.seed("seeds/MBnB.sql")
    repository = SpaceRepository(db_connection)
    assert repository.all() == [
        Space(1, 'Cottage', 'A nice cottage', 27.50, 4),
        Space(2, 'Villa', 'A mediterranean villa with a sea view', 70.00, 2),
        Space(3, 'Alpine lodge', 'A cosy ski lodge with wood-burning fire', 95.00, 3),
        Space(4, 'Studio Apartment', 'A cool apartment in the centre of the bustling city', 102.00, 3),
        Space(5, 'Tent', 'A tent in a field of cows', 10.00, 2)
    ]


def test_create_a_new_space(db_connection):
    db_connection.seed("seeds/MBnB.sql")
    repository = SpaceRepository(db_connection)
    repository.create(Space(None, 'Studio Flat', 'A cool city-centre location', 50.00, 3))
    assert repository.all() == [
        Space(1, 'Cottage', 'A nice cottage', 27.50, 4),
        Space(2, 'Villa', 'A mediterranean villa with a sea view', 70.00, 2),
        Space(3, 'Alpine lodge', 'A cosy ski lodge with wood-burning fire', 95.00, 1),
        Space(4, 'Studio Flat', 'A cool city-centre location', 50.00, 3)
    ]

def test_find_space_by_name_returns_single_space(db_connection):
    db_connection.seed("seeds/MBnB.sql")
    repository = SpaceRepository(db_connection)
    space = repository.find_by_name("Alpine lodge")
    assert space == Space(3, 'Alpine lodge', 'A cosy ski lodge with wood-burning fire', 95.00)