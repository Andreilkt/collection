"""Скрипт работа со словарем"""

library = {}

desk = {"author": "Л. Толстой", "year": "1869", "genre": "Роман"}
library ["Война и мир"] = desk
#print(library)

a = library.values()

#b = library.get("Война и мир", )

print(a)



