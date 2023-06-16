
class User:
    def __init__(self, username):
        self.username = username
        self.password = None

    def set_password(self, password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        self.password = password
        print("Password set successfully for user", self.username)

    def check_password(self, password):
        if self.password is None:
            raise ValueError("Password has not been set yet")
        if password != self.password:
            raise ValueError("Incorrect password")
        print("Password is correct for user", self.username)



