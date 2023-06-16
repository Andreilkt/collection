class User:
    def __init__(self, name, number_passport):
        self._name: str = name
        self._age: int = 1
        self._number_passport: int = number_passport
        self.__password: str = None
        self._balanse: int = 0


    @property
    def set_passwd(self) -> str:
        if self.__password == "password":
            self.__password = "asdfghj"
            return f"{self.__password = asdfghj}"

        else:
            raise ValueError("Пароль уже назначен")

    def check_passwd(self) -> None:
        if self.__password =="asdfghj":
            print("Пароль совпадает")
        else:
            raise ValueError("Пароль не прошел проверку")


user_info = User("Sergey", "1", "asdfghj")

#a = user_info.check_passwd()
#print(a)



print(user_info.check_passwd)
print(user_info._age)

user_info._age = 45





class buyer():
    pass

class salesman():
    pass
