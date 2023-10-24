class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        attributes_string = ", ".join(
            repr(attribute) for attribute in [
                self.id,
                self.username,
                self.password
            ]
        )
        return f"User({attributes_string})"
