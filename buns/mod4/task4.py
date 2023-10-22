def is_palindrome_possible(word):
    char_count = {}

    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    odd_count = 0
    odd_char = ''

    for char, count in char_count.items():
        if count % 2 != 0:
            odd_count += 1
            odd_char = char
        if odd_count > 1:
            return False

    palindrome = ''
    for char, count in char_count.items():
        palindrome += char * (count // 2)

    if odd_count == 1:
        palindrome += odd_char

    palindrome += palindrome[::-1]

    return palindrome


word = input("Введите слово: ")
result = is_palindrome_possible(word)
if result:
    print("Можно составить:", result)
else:
    print("Невозможен")