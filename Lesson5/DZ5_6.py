lesson_dict = {}
with open("file.txt", encoding='utf-8') as f:
    for line in f:
        hours = 0
        new_str = line.split()
        for word in new_str[1:]:
            index = word.find('(')
            if index >= 0:
                hours += int(word[:index]) # Число находится непосредственно перед открывающейся скобкой
        lesson_dict[new_str[0].strip(':')] = hours

print(lesson_dict)
