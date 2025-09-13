import stats

def main():
    book_source = "books/frankenstein.txt"
    book_text = stats.get_book_text(book_source)
    char_count = stats.count_chars(book_text)
    sorted_list = stats.sort_list(book_text)

    # word_count = stats.count_words(book_text)
    # print(f"{word_count} words found in the document")

    print(f"{char_count}")
    print(f"{sorted_list}")

main()
