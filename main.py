from stats import get_num_words
from stats import get_num_chars
from stats import get_chars_dict


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    chars = get_chars_dict(text)
    print(f"{num_words} words found in the document")
    print(num_chars)
#    print(chars)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
