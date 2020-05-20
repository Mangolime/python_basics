with open('file.txt', 'w') as file_out:
    while True:
        new_str = input("Введите текст или ничего не вводите для завершения: ")
        if new_str == "":
            break
        else:
            file_out.write(f"{new_str}\n")
