rating = [12, 9, 7, 4, 2]
while True:
    num = int(input('Введите следующее натуральное число либо -1 для окончания: '))
    if num != -1:
        i = 0
        while i < len(rating):
            if num <= rating[i]:
                i += 1
            else:
                break
        rating.insert(i, num)
    else:
        break
print(rating)
