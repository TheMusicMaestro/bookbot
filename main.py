from stats import count_chars, sort_list
# from stats import count_words

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_source = "books/frankenstein.txt"
    book_text = get_book_text(book_source)
    char_count = count_chars(book_text)
    # word_count = count_words(book_text)
    # print(f"{word_count} words found in the document")
    print(f"{char_count}")
    print(f"{sort_list}")

main()
