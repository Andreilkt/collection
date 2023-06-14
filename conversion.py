class Conversion():
  def __init__(self,mililiters):
    self.mililiters = mililiters

  def convert(self):
    self.liters = self.mililiters / 1000
    return self.liters

# Создадим экземпляр класса с 500 милилитрами
example = Conversion(500.0)
# Конвертируем милилитры в литры
liters = example.convert()
print('500 милилитров =', liters, 'литров')
