import json

firm_dict = {}  # Словарь с фирмами
income = 0  # Суммарная прибыль (без учета фирм с убытками)
num = 0  # Количество фирм
with open("file.txt", encoding='utf-8') as f_in:
    for line in f_in:
        firm = line.split()
        new_income = float(firm[2]) - float(firm[3])
        firm_dict[firm[0]] = new_income
        if new_income >= 0:
            num += 1
            income += new_income
    firm_list = [firm_dict, {"average_profit": income / num}]
    print(firm_list)
with open("file.json", "w") as f_out:
    json.dump(firm_list, f_out)
