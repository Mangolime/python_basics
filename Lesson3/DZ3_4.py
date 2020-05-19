def my_func(x, y):
    res1 = x ** y
    res2 = 1
    for i in range(-y):
        res2 *= x
    return res1, 1 / res2


x1 = float(input("Введите действительное положительное число x: "))
y1 = int(input("Введите целое отрицательное число y: "))
print(my_func(x1, y1))
