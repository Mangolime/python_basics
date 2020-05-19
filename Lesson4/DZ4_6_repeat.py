from sys import argv
from itertools import cycle


my_list = argv[1:]  # получаем список из параметров скрипта
i = 0 # количество выведенных значений
for el in cycle(my_list):
    if i >= 20:
        break
    else:
        print(el)
        i += 1
