revenue = float(input('Введите выручку: '))
costs = float(input('Введите издержки: '))
profit = revenue - costs
if profit > 0:
    print('Прибыль:', profit)
    print('Рентабельность выручки:', profit / revenue)
    employee_num = int(input('Введите численность сотрудников: '))
    print('Прибыль в расчете на одного сотрудника:', profit / employee_num)
elif profit < 0:
    print('Убыток:', -profit)
