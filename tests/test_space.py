from lib.spaces import Space

"""
Check Space constructs
"""
def test_new_space_constructs_correctly():
    space = Space(1, "Cottage", "A relaxing cottage", 27.50)
    assert space.id == 1
    assert space.name == "Cottage"
    assert space.description == "A relaxing cottage"
    assert space.price == 27.50

"""
Check string representation
"""
def test_new_space_displays_nicely():
    space = Space(1, "Cottage", "A relaxing cottage", 27.50)
    assert str(space) == "Space(1, Cottage, A relaxing cottage, 27.5)"

"""
Check 2 spaces with same attributes are equal
"""
def test_spaces_are_equal():
    space1 = Space(1, "Cottage", "A relaxing cottage", 27.50)
    space2 = Space(1, "Cottage", "A relaxing cottage", 27.50)
    assert space1 == space2

"""
Check validity of newly created Space using form
"""

"""
Generate errors when form filled out incorrectly
"""
