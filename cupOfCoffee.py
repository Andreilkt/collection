class CupOfCoffee:
    """Стакан кофе
    """
    DEFAULT_SIZE_ML: int = 250

    def __init__(self, size_ml: int = DEFAULT_SIZE_ML):
        """Конструктор класса чашка кофе
        """
        self._size_ml: int = size_ml
        self._filled_ml: int = 0

    def status(self) -> str:
        """  :return: Объем кофе / объем стакана

        """
        return f"{self._filled_ml / self._size_ml}"
    def fill(self, ml: int) -> None:
        """Наполнить стакан
           :param ml: Объем кофе (мл)
        """
        if ml > self._size_ml - self._filled_ml:
            raise ValueError("Слишком много кофе")
        self._filled_ml += ml
    def drink(self, ml_drunk: int) -> None:
        """Выпить кофе
        :param ml_drunk: Выпитый кофе (мл)"""
        if ml_drunk > self._size_ml - self._filled_ml:
            raise ValueError("Кофе не осталось")
            self._filled_ml -= ml_drunk


