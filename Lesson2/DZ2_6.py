goods = []
i = 1
while True:
    name = input('Введите название товара либо -1 для завершения: ')
    if name == '-1':
        break
    else:
        price = int(input('Введите цену товара: '))
        quant = int(input('Введите количество товара: '))
        unit = input('Введите единицы измерения: ')
        goods.append((i, {'название': name, 'цена': price, 'количество': quant, 'ед': unit}))
        i += 1
stats = {}
for el in goods[0][1].keys():
    stats[el] = list(set((item[1][el]) for item in goods))
print(goods)
print(stats)
