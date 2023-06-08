"""Скрипт калькулятора с простыми действиями"""


# Сложение
def sum(x, y):
    return x + y


# Вычитание
def subtract(x, y):
    return x - y


# Умножение
def multiply(x, y):
    return x * y


# Деление
def divide(x, y):
    if y == 0:
        print("На ноль делить нельзя!")
        return None
    else:
        return x / y


print("Выберите операцию.")
print("+ - Сложение")
print("- - Вычитание")
print("* - Умножение")
print("/ - Деление")

# Запросить у пользователя ввод номера операции.
choice = input("Введите номер операции (+, -, *, /): ")

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

if choice == '+':
    print(num1, "+", num2, "=", sum(num1, num2))

elif choice == '-':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '*':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '/':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Некорректный ввод")
