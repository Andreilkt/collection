""" Этот файл содержит класс CupOfCoffee, Создание Объектов этого класса,  и обращение к методам класса
"""


# Класс CupOfCoffee
class CupOfCoffee:
    """Стакан кофе
    """
    DEFAULT_SIZE_ML: int = 250

    def __init__(self, size_ml: int = DEFAULT_SIZE_ML):
        """Конструктор класса чашка кофе
        """
        self._size_ml: int = size_ml
        self._filled_ml: int = 100
        # Количество выпитого кофе
        self._drunk_ml: int = 0

    def status(self) -> str:
        """  :return: Объем кофе / объем стакана
        """
        return f"{self._filled_ml / 1000} / {self._size_ml / 1000}"

    def fill(self, ml: int) -> None:
        """Наполнить стакан
           :param ml: Объем кофе (мл)
        """
        if ml > self._size_ml - self._filled_ml:
            raise ValueError("Слишком много кофе")
        else:
            print("Можно еще налить")
        self._filled_ml += ml

    def drink(self, ml_drunk: int) -> None:
        """Выпить кофе
        :param ml_drunk: Выпитый кофе (мл)"""
        if ml_drunk >= self._filled_ml - self._drunk_ml:
            raise ValueError("Кофе не осталось")
            self._filled_ml -= ml_drunk
        else:
            print("Кофе еще есть")


# Вызов конструктора
cup_of_coffee = CupOfCoffee()

# Обращение к методам класса CupOfCoffee
cup_of_coffee.fill(50)

status = cup_of_coffee.status()
print(status)

cup_of_coffee.drink(120)

status = cup_of_coffee.status()
print(status)
