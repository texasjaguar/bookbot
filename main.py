import sys
from stats import get_num_words, count_characters, sort_by_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    c = get_num_words(get_book_text(sys.argv[1]))
    count_c = count_characters(get_book_text(sys.argv[1]))
    count_list = sort_by_count(count_c)
    print (f'''============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {c} total words
--------- Character Count -------''')
    for character in count_list:
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")
    
main()