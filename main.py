from stats import count_words
from stats import count_chars

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    # define variables
    book_source = "books/frankenstein.txt"
    book_text = get_book_text(book_source)
    word_count = count_words(book_text)
    char_count = count_chars(book_text)
    # print content to console
    print(f"{word_count} words found in the document")
    print(f"{char_count}")

main()
