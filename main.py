def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(book_text):
    split_words = book_text.split()
    total_words = 0
    for word in split_words:
        total_words += 1
    return total_words

def main():
    # define variables
    book_source = "books/frankenstein.txt"
    book_text = get_book_text(book_source)
    word_count = count_words(book_text)

    # print content to console
    print(f"{book_text}")
    print(f"{word_count} words found in the document")

main()
