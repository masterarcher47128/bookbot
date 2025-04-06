from stats import *

def get_book_text(file) :
    with open(file) as f:
        return f.read()
    
def main():
    filepath = "books/test.txt"
    book_text = get_book_text(filepath)

    word_count = count_words(book_text)
    letter_count = count_characters(book_text)

    create_report(filepath, word_count, letter_count)

main()