from stats import get_num_words
from stats import get_num_chars


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    print(f"{num_words} words found in the document")
    print(f"{num_chars} chars found in the document")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
