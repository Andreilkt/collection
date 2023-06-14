class Person(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print(f'Hello, my name is {self.name}')

  def birth_year(self):
    print(f'I was born in {2021 - self.age}')

# Объявить новый объект Person
person1 = Person("John", 36)

# Вызвать методы
person1.greet()
person1.birth_year()




