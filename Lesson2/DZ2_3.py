month_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень',
              'Зима']
month_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето',
              9: 'Осень', 10: 'Осень', 11: 'Осень',
              12: 'Зима'}
month = int(input('Введите порядковый номер месяца: '))
print(f'Определение времени года с помощью списка: {month_list[month - 1]}')
print(f'Определение времени года  с помощью словаря: {month_dict[month]}')
