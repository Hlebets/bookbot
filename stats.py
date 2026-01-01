def get_num_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    print(f"Found {num_words} total words")


def get_num_characters(file_contents):
    dict_characters = {}
    lowerfile_contents = file_contents.lower()
    for char in lowerfile_contents:
        if char in dict_characters:
            dict_characters[char] += 1
        else:
            dict_characters[char] = 1
    for char, count in dict_characters.items():
        print(f"{repr(char)}: {count}")
