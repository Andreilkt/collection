
""" Скрипт принимает числа через пробел от пользователя и делит их на два списка четный и нечетный"""

# Ввод чисел через пробел
numbers = input('Введите числа через пробел:').split()
# Преобразование к целому числу и запись в список
numbers = [int(number) for number in numbers]
# Вывод неразделенного списка
print("Неразделенный список",numbers)

# Создаем два пустых списка
even_numbers = []
odd_numbers = []
# Проход по списку чисел. и разделение его на четные и нечетные числа
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# Выводы четного и нечетного списков
print("Список четных:", even_numbers)
print("Список нечетных:", odd_numbers)
