import os
from stats import get_num_words, get_num_characters, sort_characters_by_count


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def main():
    get_num_words(get_book_text("books/frankenstein.txt"))
    get_num_characters(get_book_text("books/frankenstein.txt"))
    sort_characters_by_count(get_book_text("books/frankenstein.txt"))


if __name__ == "__main__":
    main()
