def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return

a = input('Введите первое число: ')
b = input('Введите второе число: ')
res = division(float(a), float(b))
print(f'{a}/{b} = {res}') if res is not None else print('Деление на ноль')
