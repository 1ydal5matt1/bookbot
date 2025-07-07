from stats import get_num_words
from stats import count_char

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def main():
    words_in_book = get_num_words(get_book_text("books/frankenstein.txt"))
    print(f"{words_in_book} words found in the document")
    print(count_char(get_book_text("books/frankenstein.txt")))








if __name__ == "__main__":
    main()