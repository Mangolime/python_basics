file_in = open("file.txt", encoding='utf-8')
file_out = open("file_out.txt", "w", encoding='utf-8')
num_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
for line in file_in:
    for key in num_dict:
        if key in line:
            new_line = line.replace(key, num_dict[key])
    file_out.write(new_line)
file_in.close()
file_out.close()
