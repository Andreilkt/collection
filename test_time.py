
from datetime import datetime
import pytz


class Moscow:
    @property
    def local_time(self):
        tz = pytz.timezone('Europe/Moscow')
        return datetime.now(tz=tz)


class Ekaterinburg:
    @property
    def local_time(self):
        tz = pytz.timezone('Asia/Yekaterinburg')
        return datetime.now(tz=tz)


class Vladivostok:
    @property
    def local_time(self):
        tz = pytz.timezone('Asia/Vladivostok')
        return datetime.now(tz=tz)

moscow = Moscow()
ekaterinburg = Ekaterinburg()
vladivostok = Vladivostok()

print("Москва:", moscow.local_time)
print("Екатеринбург:", ekaterinburg.local_time)
print("Владивосток:", vladivostok.local_time)


"""
Каждый из классов имеет свойство `local_time`, которое возвращает текущее время в 
соответствующем городе. Для работы с часовыми поясами мы используем библиотеку `pytz`.

"""
