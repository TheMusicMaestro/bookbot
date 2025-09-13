def count_words(book_text):
    split_words = book_text.split()
    total_words = 0
    for word in split_words:
        total_words += 1
    return total_words

def count_chars(book_text):
    char_dict = {}
    lower_chars = book_text.lower()
    for char in lower_chars:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_list(char_dict):
    sorted_list = {}
    
    return sorted_list