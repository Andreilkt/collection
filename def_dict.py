"""Скрипт содержит две функции, одна добавляет в пустой словарь данные.
вторая выводит данные из словаря"""

# функция для добавления даных в словарь library
library = {}


def add_book(title, author, year, genre):
    # создаем словарь с информацией о книге
    desk = {"author": author, "year": year, "genre": genre}
    # добавляем информацию о книге в словарь library
    library[title] = desk
    return library


# функция для вывода всех книг в словаре library
def print_books():
    for title, desk in library.items():
        author = desk["author"]
        year = desk["year"]
        genre = desk["genre"]
        print(f"{title} — {author} ({year}, {genre})")


add_book("Война и мир", "Л. Толстой", 1869, "Роман")
add_book("Преступление и наказание", "Ф. Достоевский ", 1866, "Роман")
add_book("Мастер и маргарита", "М. Булгаков", 1967, "Роман")
add_book("1984", "Дж. Оруэл", 1949, "антиутопия")

# выводим все книги в словаре library
print_books()
