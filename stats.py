def get_num_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    print(f"Found {num_words} total words")


def sort_on(dict_item):
    return dict_item["num"]


def get_num_characters(file_contents):
    dict_characters = {}
    for char in file_contents.lower():
        dict_characters[char] = (
            dict_characters[char] + 1 if char in dict_characters else 1
        )
    return dict_characters


def sort_characters_by_count(dict_characters):
    sorted_list = []
    for char in dict_characters:
        sorted_list.append({"char": char, "num": dict_characters[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
