import sys

from stats import *


def get_book_text(path):
    content = None
    with open(path) as f:
        content = f.read()
    return content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    content = get_book_text(book_path)
    num_words = word_count(content)
    num_chars = char_count(content)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in mapping_char_count_dict(num_chars):
        if(item["char"].isalpha()):
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
