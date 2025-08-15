
import sys
from stats import (
 words_count,
 character_count,
 build_sorted_list
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_counter = words_count(text)
    character_counter = character_count(text)
    report = build_sorted_list(text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_counter} total words")
    print("--------- Character Count -------")

    for entry in report :
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

    

def get_book_text(path):
    with open(path) as f:
        return f.read()

 



main()
