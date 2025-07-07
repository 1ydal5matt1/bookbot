from stats import get_num_words
from stats import count_char
from stats import sort_dict
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    # book_loc = "books/frankenstein.txt"
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_loc = sys.argv[1]
        words_in_book = get_num_words(get_book_text(book_loc))
        char_dict = sort_dict(count_char(get_book_text(book_loc)))
        # print(f"{words_in_book} words found in the document")
        # print(sort_dict(count_char(get_book_text("books/frankenstein.txt"))))

        print("============ BOOKBOT ============")    
        print(f"Analyzing book found at {book_loc}...")
        print("----------- Word Count ----------")
        print(f"Found {words_in_book} total words")
        print("--------- Character Count -------")
        for i in char_dict:
            if str(i[0]).isalpha():
                print(f"{i[0]}: {i[1]}")
        print("============= END ===============")
        sys.exit(0)


if __name__ == "__main__":
    main()