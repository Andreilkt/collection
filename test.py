class CoffeeMug:
    def __init__(self, inscription, milliliters=0):
        self.inscription = inscription
        self.milliliters = milliliters

    #template for the class descriptor
    class InscriptionValidator:
      def __init__(self, max_length):
          self.max_length = max_length
      def __set__(self, instance, value):
          if len(value) > self.max_length:
              raise InscriptionError(f"Длина инскрипции слишком длинная! Превышен максимальный длинной на {len(value)-self.max_length} символов")
          else:
              instance.inscription = value

    #validator with max length of 15
    max_length = 15
    inscription = InscriptionValidator(max_length)

    #setter and getter methods
    def set_inscription(self, inscription):
        self.inscription = inscription

    def get_inscription(self):
        return self.inscription

    def set_filled_milliliters(self, milliliters):
        self.milliliters = milliliters

    def get_filled_milliliters(self):
        return self.milliliters

#создаем чашку с инскрипцией
mug = CoffeeMug("Привет мир!")
#устанавливаем наполненность чашки
mug.set_filled_milliliters(1000)

#пытаемся задать инскрипцию, превышающую максимальную длинну
try:
    mug.inscription = "Еще одна очень длинная инскрипция!"
except InscriptionError as e:
    print(e)test1
