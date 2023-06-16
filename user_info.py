
class User_info:
    def __init__(self, name):
        self.name = name
        self.__password = None

    def set_password(self, password):
        if len(password) < 10:
            raise ValueError(" ВВедите не меньше 10 символов")
        self.__password = password
        print("Пароль установлен", self.username)

    def check_password(self, password):
        if self.__password is None:
            raise ValueError("Пароль не установлен")
        if password != self.__password:
            raise ValueError("Пароль не прошел проверку")
        print("Пароль прошел проверку", self.username)



