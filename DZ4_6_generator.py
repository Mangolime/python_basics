from sys import argv
from itertools import count


num = int(argv[1])  # получаем начальное число из параметров скрипта
i = 0 # количество сгенерированных значений
for el in count(num):
    if i >= 20:
        break
    else:
        print(el)
        i += 1
