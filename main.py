from stats import word_count, sort_char_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    #print(get_book_text("./books/frankenstein.txt"))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    word_count(book_text)
    print("--------- Character Count -------")
    sort_char_list(book_text)
    print("============= END ===============")


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_text = get_book_text(sys.argv[1])

main()
