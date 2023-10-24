from lib.user import User

"""
WHEN: we create an instance of `User`
AND:  we provide the required arguments
THEN: it creates a new instance of `User`
"""
def test_can_construct_user():
    user = User(id=None, username=None, password=None)
    assert isinstance(user, User)

