import sys
from stats import get_num_words
from stats import get_num_chars
from stats import sort_chars


def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        num_chars = get_num_chars(text)
        sorted_chars = sort_chars(num_chars)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("----------- Character Count ----------")
        for item in sorted_chars:
            print(f"{item['char']}: {item['num']}")
    else:
        sys.exit("Usage: python3 main.py <path_to_book>")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
