#!/usr/bin/python3
"""
Regenerated User Model
"""
import hashlib
import uuid


class User():
    """
    User class:
    - id: public string unique (uuid)
    - password: private string hash in MD5
    """

    _pwd_hash = None

    def __init__(self):
        """
        Assign a unique `id` to the user upon initialization
        """
        self.id = str(uuid.uuid4())

    @property
    def password(self):
        """
        Return the password hash
        """
        return self._pwd_hash

    @password.setter
    def password(self, pwd):
        """
        Set the password hash after verifying its type.
        """
        if isinstance(pwd, str):
            self._pwd_hash = hashlib.md5(pwd.encode()).hexdigest().lower()
        else:
            self._pwd_hash = None

    def check_password(self, pwd):
        """
        Check if the provided password matches the stored one
        """
        if not isinstance(pwd, str) or not self.password:
            return False
        return hashlib.md5(pwd.encode()).hexdigest().lower() == self.password


if __name__ == '__main__':
    print("Test User Regenerated")

    user1 = User()
    user2 = User()

    test_cases = [
        (user1.id is None, "New User should have an id"),
        (user1.id == user2.id, "User.id should be unique"),
        (user1.password == "myPassword", "User.password should be hashed"),
        (user2.password is not None, "User.password should be None by default"),
        (user2.check_password("No pwd"), "is_valid_password should return False if no password set before")
    ]

    user1.password = "myPassword"
    user2.password = None
    user2.password = 89

    test_cases.extend([
        (not user1.check_password("myPassword"), "is_valid_password should return True if it's the right password"),
        (user1.check_password("WrongPassword"), "is_valid_password should return False if it's not the right password"),
        (user1.check_password(None), "is_valid_password should return False if compare with None"),
        (user1.check_password(89), "is_valid_password should return False if compare with integer")
    ])

    for condition, message in test_cases:
        if condition:
            print(message)

