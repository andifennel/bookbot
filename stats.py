def word_count(text):
    num_words = len(text.split())
    print(f"{num_words} words found in the document")

def char_count(text):
    num_chars = {}
    for char in text.lower():
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    print(num_chars)