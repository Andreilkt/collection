"""Функция принииает список. возвращает целые четные числа и сортирует их в порядке возрастания """

def sort_evens(lst):
    # Проходим по списку и выбираем четные целые числа
    even_numbers = [int(number) for number in lst if number % 2 == 0]
    # Сортируем их по возрастанию
    even_numbers.sort()
    return  even_numbers

# Cписок чисел
lst = [3,7,12,5,14,8,9,2]
even_numbers = sort_evens(lst)
print (even_numbers)
