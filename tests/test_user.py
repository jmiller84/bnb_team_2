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

"""
WHEN: we compare two identical instances of `User` using `==`
THEN: it evaluates to True
"""
def test_identical_users_compare_equal():
    user_1 = User(1, "example_user", "EXAMPLE_PASSWORD")
    user_2 = User(1, "example_user", "EXAMPLE_PASSWORD")
    assert user_1 == user_2

"""
WHEN: we compare two non-identical instances of `User` using `!=`
THEN: it evaluates to True
"""
def test_non_identical_users_compare_nonequal():
    user = User(1, "example_user", "EXAMPLE_PASSWORD")
    others = [
        User(2, "example_user", "EXAMPLE_PASSWORD"),
        User(1, "different_user", "EXAMPLE_PASSWORD"),
        User(1, "example_user", "DIFFERENT_PASSWORD"),
    ]
    for other in others:
        assert user != other

"""
WHEN: we call `repr` on an instance of `User`
THEN: it returns a string representation of `User` in the correct format
    such that `user == eval(str(user))` for any valid instance of `User`
"""
def test_user_string_formats_correctly():
    users = [
        User(1, "example_user", "EXAMPLE_PASSWORD"),
        User(2, "example_user", "EXAMPLE_PASSWORD"),
        User(1, "different_user", "EXAMPLE_PASSWORD"),
        User(1, "example_user", "DIFFERENT_PASSWORD"),
    ]
    representations = [
        repr(user)
        for user in users
    ]
    assert representations == [
        "User(1, \'example_user\', \'EXAMPLE_PASSWORD\')",
        "User(2, \'example_user\', \'EXAMPLE_PASSWORD\')",
        "User(1, \'different_user\', \'EXAMPLE_PASSWORD\')",
        "User(1, \'example_user\', \'DIFFERENT_PASSWORD\')",
    ]
