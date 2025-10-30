import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    text = get_book_text(sys.argv[1])
    from stats import count_words
    from stats import count_chars
    from stats import sorted_list
    word_count = count_words(text)
    char_count = count_chars(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list(char_count):
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")
    print("============= END ===============")

main()