with open("file.txt", encoding='utf-8') as f:
    content = f.readlines()
    print("Общее количество строк: ", len(content))
    for num, line in enumerate(content):
        print(f"Строка {num + 1} - количество слов {len(line.split())}")
