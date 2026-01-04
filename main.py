import sys
from stats import get_num_words, get_num_characters, sort_characters_by_count


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents





def main():
    if len(sys.argv) == 2:
        path_to_book = sys.argv[1]
        chars_dict = get_num_characters(get_book_text(path_to_book))
        chars_sorted_list = sort_characters_by_count(chars_dict)        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_book}...")
        print("----------- Word Count ----------")
        get_num_words(get_book_text(path_to_book))
        print("--------- Character Count -------")
        for item in chars_sorted_list:
            if item["char"].isalpha():
                print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
        sys.exit(0)
        return
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


if __name__ == "__main__":
    main()
