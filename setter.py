# Источник: https://pythonpip.ru/osnovy/gettery-settery-python

class Javatpoint:
     def __init__(self):
          self._age = 0

     # using the getter function
     @property
     def age(self):
         print("getter method")
         return self._age

     #now, using the setter function
     @age.setter
     def age(self, x):
         if(x < 20):
            raise ValueError("the age is below eligibility criteria")
         print("setter method")
         self._age = x

John = Javatpoint()

John.age = 25

print(John.age)
