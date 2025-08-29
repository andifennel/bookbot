from stats import word_count, char_count

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    print(get_book_text("./books/frankenstein.txt"))
    word_count(get_book_text("./books/frankenstein.txt"))
    char_count(get_book_text("./books/frankenstein.txt"))
    
main()
