"""Класс для сохдания и проверки пароля пользователя"""


class User_info:
    # Конструктор класса
    def __init__(self, name, balans):
        self.name: str = name
        self.age: int = 1
        self.hobbies = None
        self.__password = None
        self.balans: int = balans

    # Установка Пароля
    def set_password(self, password):
        if len(password) < 10:
            raise ValueError(" Не меньше  10 символов")
        self.__password = password
        print("Пароль установлен", self.name)

    # Проверка пароля
    def check_password(self, password):
        if self.__password is None:
            raise ValueError("Пароль не установлен")
        if password != self.__password:
            raise ValueError("Пароль не прошел проверку")
        print("Пароль прошел проверку", self.name)

    # Добавление хобби
    def check_hobbies(self, hobbies):
        if hobbies is None:
            print("Хобби нет")
        hobby = self.hobbies = hobbies
        print("У Вас хобби",hobby, self.name)


# Создаем объект класса Password
user = User_info("Sergey")

#Добавление возраста
info = user.age = 45
print(info)

#Добавление хобби
hobby = user.check_hobbies("")
print(hobby)

#  Установка пароля
try:
    user.set_password("qwertyuiop")
except ValueError as e:
    print(e)

try:
    user.set_password("12345678")
except ValueError as e:
    print(e)

# Проврка пароля
try:
    user.check_password("qwertyuiop")
except ValueError as e:
    print(e)

try:
    user.check_password("12345678")
except ValueError as e:
    print(e)
else:
    print("Пароль некорректный")

class buyer(User_info):
    pass

class salesman(User_info):
    pass
