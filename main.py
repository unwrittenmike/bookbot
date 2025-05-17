import sys
from stats import get_num_words, get_caracter_counts, get_sorted_counts

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book = get_book_text(path)
    num_words = get_num_words(book)
    caracter_counts = get_caracter_counts(book)
    sorted_counts = get_sorted_counts(caracter_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for stat in sorted_counts:
        if stat["char"].isalpha():
            print(f"{stat['char']}: {stat['num']}")
    print("============= END ===============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

main()
