class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(username, password):
        return username == "admin" and password == "password"