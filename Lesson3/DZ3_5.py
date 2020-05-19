my_sum = 0
while True:
    numb = input("Введите числа, разделенные пробелом, либо символ q для завершения: ").split()
    try:
        ind = numb.index('q')
        my_sum += sum(map(float, numb[:ind]))
        print(my_sum)
        break
    except ValueError:
        my_sum += sum(map(float, numb))
        print(my_sum)
