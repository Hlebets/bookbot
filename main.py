import os

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def count_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    print(f"Found {num_words} total words")

def main():
    count_words(get_book_text("books/frankenstein.txt"))

if __name__ == "__main__":
    main()