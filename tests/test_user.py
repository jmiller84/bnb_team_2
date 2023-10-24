from lib.user import User

"""
WHEN: we create an instance of `User`
AND:  we provide the required arguments
THEN: it creates a new instance of `User`
"""
def test_can_construct_user():
    user = User(id=None, username=None, password=None)
    assert isinstance(user, User)

"""
WHEN: we create an instance of `User`
AND:  we provide the required arguments
THEN: the created instance of `User` has attribute values
    corresponding to the argument values we provided
"""
def test_user_constructs_correctly():
    user = User(1, "example_user", "EXAMPLE_PASSWORD")
    assert user.id == 1
    assert user.username == "example_user"
    assert user.password == "EXAMPLE_PASSWORD"