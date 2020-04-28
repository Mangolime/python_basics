my_str = input('Введите строку из слов, разделенных пробелами: ').split()
for ind, el in enumerate(my_str):
    print(ind, el[:10])
