def count_letters(file_name):
    char_count = {}

    with open(file_name, 'r') as file:
        contents = file.read()

        for char in contents:
            if char.isalpha():
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

    # Сортируем статистику по частоте встречаемости (key=lambda помогает сортировать по количеству символов)
    sorted_count = sorted(char_count.items(), key=lambda x: x[1])

    with open('result.txt', 'w') as file:
        for char, count in sorted_count:
            file.write(f"{char}: {count}\n")


file_name = input("Введите имя файла: ")
count_letters(file_name)