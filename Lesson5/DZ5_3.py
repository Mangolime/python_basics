with open("file.txt", encoding='utf-8') as f:
    num = 0  # счетчик числа сотрудников в файле
    salary = 0  # счетчик суммарного дохода сотрудников
    print("Сотрудники с зарплатой ниже 20000:")
    for line in f:
        cur_name, cur_salary = line.split()
        if float(cur_salary) < 20000:
            print(cur_name)
        num += 1
        salary += float(cur_salary)
print(f"Средняя величина дохода сотрудников: {salary / num}")
