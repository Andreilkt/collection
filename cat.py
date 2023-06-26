
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.__password = None

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password


"""
Метод `set_password` устанавливает значение поля `__password`, 
а метод `get_password` возвращает его значение. Обратите внимание, 
что поле `__password` является приватным, то есть доступ к нему возможен только изнутри класса.
Код:
"""

class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password
        self.balance = 0

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password


class Buyer(User):
    def __init__(self, name, password):
        super().__init__(name, password)


class Seller(User):
    def __init__(self, name, password):
        super().__init__(name, password)


def transaction(user):
    if isinstance(user, Buyer):
        user.balance -= 100
    elif isinstance(user, Seller):
        user.balance += 100


buyer = Buyer("John", "1234")
seller = Seller("Jane", "5678")

transaction(buyer)
transaction(seller)

print(buyer.balance)  # -100
print(seller.balance)  # 100

"""
В данном коде мы создали базовый класс `User` с полями `name`, `__password` и `balance`. Затем мы создали два класса-наследника `Buyer` и `Seller`, которые наследуют поля и методы базового класса.

Далее мы создали функцию `transaction`, которая принимает объект класса `User`. Внутри функции мы проверяем, является ли переданный объект экземпляром класса `Buyer` или `Seller`, и в зависимости от этого увеличиваем или уменьшаем значение поля `balance`.

В конце мы создали объекты классов `Buyer` и `Seller`, передали их в функцию `transaction` и вывели значения поля `balance` для каждого из них.
"""
