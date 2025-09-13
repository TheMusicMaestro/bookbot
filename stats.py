def count_words(book_text):
    split_words = book_text.split()
    total_words = 0
    for word in split_words:
        total_words += 1
    return total_words
