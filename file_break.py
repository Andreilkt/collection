"""Скрипт принимает на вход большой файл и разбивает его на два файла. количество строк примерно можно устаовить руками"""

from pathlib import Path
import os
# читает файл в список
def read2list(file):
    # global lines
    # открываем файл в режиме чтения utf-8
    file = open(file, 'r', encoding='utf-8')
    # читаем все строки и удаляем переводы строк
    lines = file.readlines()
    lines1 = [line.rstrip() for line in lines]
    file.close()
    return lines1
lines2 = read2list('read_1.feature')
rows = len(lines2)
print("Количество строк в списке")
print(rows)
print("Неразделеный список")
print(lines2)
print(type(lines2))
sl = lines2[0:4]
print("Список 1")
print(sl)
with open('wr1.feature', 'w') as filehandle:
    for listitem in sl:
        filehandle.writelines(listitem)
sz = os.stat('read_1.feature').st_size
print(sz)
sl1 = lines2[5:]
print("Список 2")
print(sl1)
with open('wr2.feature', 'w') as filehandle:
    for listitem1 in sl1:
        filehandle.writelines(listitem1 + '\n')
sz1 = os.stat('read_1.feature').st_size
print(sz1)
