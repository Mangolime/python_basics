def my_func(a, b, c):
    num = [a, b, c]
    return sum(num) - min(num)


number = map(float, input('Введите три числа через пробел: ').split())
print(my_func(*number))
