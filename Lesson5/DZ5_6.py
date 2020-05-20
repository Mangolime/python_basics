lesson_dict = {}
with open("file.txt", encoding='utf-8') as f:
    for line in f:
        hours = 0
        new_str = line.split()
        for word in new_str[1:]:  # В цикле находим все числа - они стоят непосредственно перед открывающейся скобкой
            index = word.find('(')
            if index >= 0:
                hours += int(word[:index])
        lesson_dict[new_str[0].strip(':')] = hours  # В квадратных скобках - 1-ое слово строки, т.е. название предмета

print(lesson_dict)
