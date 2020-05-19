def int_func(word):
    return word.title()


my_str = input('Введите последовательность слов из маленьких латинских букв, разделенных пробелами: ').split()
print(*map(int_func, my_str))
