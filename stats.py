def count_words(text):
    return len(text.split())

def count_characters(text):
    unique_characters = {}
    for word in text.split():
        for char in list(word.lower()):
            if char.isalpha(): 
                if char not in unique_characters:
                    unique_characters[char] = 0
                for w in text.split():
                    unique_characters[char] += w.lower().count(char)
    sorted_unique_chars = dict(sorted(unique_characters.items(), key=lambda item: item[1], reverse=True)) # Sort by value descending
    return sorted_unique_chars


def create_report(filepath, word_count, letter_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words.")

    print("--------- Character Count -------")
    for letter, count in letter_count.items():
        print(f"{letter}: {count}")

