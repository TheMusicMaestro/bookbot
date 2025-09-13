import stats

def main():
    book_source = "books/frankenstein.txt"
    book_text = stats.get_book_text(book_source)
    word_count = stats.count_words(book_text)
    char_count = stats.count_chars(book_text)
    sorted_char_list = stats.sort_list(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_source}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted_char_list:
        char = item["char"]
        if char.isalpha():
            count = item["num"]
            print(f"{char}: {count}")

    print("============= END ===============")

main()
