# функция считывания файла в список
def read2list(file):
    # открываем файл в режиме чтения
    file = open(file, 'r', encoding='utf-8')
    # читаем все строки и удаляем переводы строк
    lines = file.readlines()
    lines1 = [line.rstrip() for line in lines]
    file.close()
    return lines1
#вызов функции
lines = read2list('read_2.txt')
#print(lines)
#поиск строки по префиксу, и запись в файл
#pr = ('  @TestCaseKey', '  Сценарий:')

#path = 'E:\\DevTransfer\\reload\\test_spel\\src\main\\resources\\'
with open('wr1.txt', 'w', encoding='utf-8') as file_for_json:
    for listitem in lines:
        #if listitem.startswith(pr):
            file_for_json.writelines(listitem.rstrip('\n') + '\\n \n')

#lines_n = read2list('wr1.feature')

#lines_n[3] = 'name'
#print(lines_n)
