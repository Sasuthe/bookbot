from stats import get_num_words, get_num_chars, sort_count
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit([1])



def main(filepath):
    ## Variables
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    count = get_num_chars(text)
    num_words = get_num_words(text)
    sorted_chars = sort_count(count)

    ## Output header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    ## Loop to display information cleanly
    print("--------- Character Count -------")
    for char_data in sorted_chars:
        char = char_data["char"]

        if char.isalpha():
            print(f"{char}: {char_data['num']}")

    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main("books/frankenstein.txt")