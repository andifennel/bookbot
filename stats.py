def word_count(text):
    num_words = len(text.split())
    print(f"Found {num_words} total words")

def char_count(text):
    num_chars = {}
    for char in text.lower():
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    return num_chars

def sort_on(items):
    return items["num"]

def sort_char_list(text):
    char_list = []
    for letter in char_count(text):
        if letter.isalpha():
            char_list.append({"char": letter, "num": char_count(text)[letter]})
    char_list.sort(reverse=True, key=sort_on)
    for dict in char_list:
        print(f"{dict['char']}: {dict['num']}")
