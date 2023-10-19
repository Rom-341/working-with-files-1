# открыть файл, получить доступ к данным и закрыть
# f = open('test1.txt')
# print(type(f))
# data = f.read()
# print(data, type(data))
# f.close()

# менеджер контекста
# def is_closed(file_):
#     if file_.closed:
#         print('Файл закрыт')
#     else:
#         print('Файл открыт')


# with open('test1.txt') as f:
#     print(type(f))
#     data = f.read()
    # is_closed(f)

# is_closed(f)


# чтение из файла
# with open('test1.txt') as f:
#     data = f.read()
#     print(type(data))
#     print(data)
#
# data += '\nЕще одно блюдо'
# print(data)


# чтение из файла по одной строке
# with open('List of recipes.txt') as f:
#     print(f.readline().strip())
#     print(f.readline().strip())
#     print(f.readline().strip())


# чтение из файла всех сразу строк
# with open('List of recipes.txt') as f:
#     lines = f.readlines()
#     print(type(lines))
#     print(len(lines))
#     print(lines[1])


# чтение из файла с помощью итерации
# with open('List of recipes.txt') as f:
#     for line in f:
#         print(line.strip())


# чтение из файла с помощью итерации одновременно по индексу и по элементу
# with open('recipes.txt', encoding= 'utf-8') as f:
#     for idx, line in enumerate(f):
#         print(idx, line.strip())


# запись в файл
# with open('test.txt', 'w') as f:
#     f.write('Привет мир!')


# чтение из файла с использованием метода read
# with open('test.txt', 'r') as f:
#     print(f.read())


# запись двух строк в файл
# with open('test.txt', 'w') as f:
#     f.write('Первая строка!\n')
##     f.write('\n')
#
# with open('test.txt', 'a') as f:
#     f.write('Вторая строка')


# режим работы с файлами:
# текстовый режим
# бинарный режим (b)
# with open('test.txt', 'rb') as f:
#     data = f.read()
#     print(type(data))
#     print(data)

# with open('test.txt', 'rb') as f:
#     print(f.readline())


# абсолютный путь к текущей директории
# import os
# import time

# print(os.getcwd())


# with open('test.txt', 'a') as f:
#     f.write(f'\n{time.time()}' '\n')
# with open('test.txt', 'r') as f:
#     print(f.read())
# # посмотрим текущую директорию
# print(os.getcwd())
#
# # построим абсолютный путь к файлу
# file_path = os.path.join(os.getcwd(), 'test.txt')
# print(file_path)


# кодировка файлов
# по умолчанию UTF-8
# with open('utf.txt', 'w', encoding='utf-8') as f:
#     f.write('Привет мир!')
#
#
# with open('utf.txt', 'r', encoding='utf-8') as f:
#     print(f.read())

# with open('cp.txt', 'w', encoding='cp1251') as f:
#     f.write('Привет мир!')

# with open('cp.txt', 'rb') as f:
#     print(f.read())

# with open('utf.txt', 'rb') as f:
#     print(f.read())
