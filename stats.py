# receives a filepath
# returns book text as string
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

# counts and returns
# the total number of words in the book
def count_words(book_text):
    split_words = book_text.split()
    total_words = 0
    for word in split_words:
        total_words += 1
    return total_words

# counts and returns a dictionary
# containing the total number of each character
def count_chars(book_text):
    char_dict = {}
    lower_chars = book_text.lower()
    for char in lower_chars:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

# receives an unsorted char_dict
# returns a sorted list from greatest to least
def sort_list(char_dict):
    char_list = []

    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})

    def sort_on(d):
        return d["num"]

    char_list.sort(key=sort_on, reverse=True)
    return char_list

