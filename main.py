from stats import *
import sys

def get_book_text(file) :
    with open(file) as f:
        return f.read()

def get_book_path():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    return book_path

def main():
    filepath = get_book_path()
    book_text = get_book_text(filepath)

    word_count = count_words(book_text)
    letter_count = count_characters(book_text)

    create_report(filepath, word_count, letter_count)

main()