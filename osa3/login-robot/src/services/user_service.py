from entities.user import User

MIN_LENGTH = 5

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)
        self.check_length(username,password)
        self.check_whitespace(username)
        self.check_digits(password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

    def check_length(self,username, password):
        if len(username) < MIN_LENGTH:
            raise UserInputError("Username is too short")
        if len(password) < MIN_LENGTH:
            raise UserInputError("Password are is too short")
    
    def check_whitespace(self, username):
        if (' ' in username):
            raise UserInputError("Username not valid, can't include ' '")

    def check_digits(self, password):
        if any(char.isdigit() for char in password):
            return
        else:
            raise UserInputError("Password needs to include numbers")
