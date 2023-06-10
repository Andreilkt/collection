class CupOfCoffee:
    """Стакан кофе"""
    DEFAULT_SIZE_ML: int = 200

    def __init__(self, size_ml: int = DEFAULT_SIZE_ML):
        """Конструктор класса"""
        self._size_ml: int = size_ml
        self._filled_ml: int =0

