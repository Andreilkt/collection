class User():
    def __init__(self, name, number_passport, password):
        self._name: str = name
        self._age: int = 1
        self._number_passport: int = number_passport
        self._password: str = " "
        self._balanse: int = 0


    def set_passwd(self, passwd: str) -> str:
        if passwd == " ":
            self._password = ""
        else:
            raise ValueError("Пароль уже назначен")

    def  check_passwd(self, passwd: str)-> str:
        if passwd == " ":
            print("Пароль совпадает")
        else:
            raise ValueError("Пароль не прошел проверку")



user_info = User("Sergey","123456", " 1")

user_info.company = "lkt"

print(user_info.company)

print(user_info._name)
print(user_info._age)

user_info._age = 45

print(user_info._age, user_info._number_passport, user_info._password)



