def count_words(text):
    return len(text.split())

def count_characters(text):
    unique_characters = {}
    for word in text.split():
        for char in list(word.lower()):
            unique_characters[char] = text.count(char)
    return unique_characters


def create_report(filepath, word_count, letter_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words.")

    print("--------- Character Count -------")
    sorted_letter_count = dict(sorted(letter_count.items(), key=lambda item: item[1]))
    for letter in sorted_letter_count:
        if letter.isalpha():
            print(f"{letter}: {word_count[letter]}")

