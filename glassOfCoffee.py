"""Класс содержит метод для создания надписи на стакане,
с проверкой, и свойство которое определяет сколько кофе в стакане"""


class glassOfCoffee:
    def __init__(self, inscription, filled_ml):
        self.inscription = inscription
        self.filled_ml = filled_ml

    @property
    def inscription(self):
        return self._inscription

    # Проверка количества символов в надписи
    @inscription.setter
    def inscription(self, inscription):
        self._inscription = inscription
        if len(inscription) > 10:
            raise ValueError(f"Inscription {inscription} Слишком длинная надпись")

    # Свойство для определения количества кофе
    @property
    def filled_ml(self):
        return self._filled_ml

    @filled_ml.setter
    def filled_ml(self, filled_ml):
        self._filled_ml = filled_ml


# Создание объекта
glass = glassOfCoffee(inscription="Hello!", filled_ml=200)

# Вы можете устанавливать и получать значения inscription и filled_milliliters с помощью геттеров и сеттеров:

# Вызов методов
glass.inscription = "Надпись"
print(glass.inscription)

glass.filled_ml = 300
print(glass.filled_ml)
