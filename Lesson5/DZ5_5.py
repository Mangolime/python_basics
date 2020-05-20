from random import random

# Генерируем 50 случайных чисел в диапазоне от 0 до 10 и записываем в файл
with open('file.txt', 'w', encoding='utf-8') as f:
    for i in range(50):
        f.write(f"{str(random() * 10)} ")


# Подсчитываем среднее значение
with open('file.txt', encoding='utf-8') as f:
    print("Сумма чисел:", sum(map(float, f.readline().split())))
