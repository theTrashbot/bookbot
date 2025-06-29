from stats import *
import sys

def sort_on(items):
    return items["num"]

def main():
    argz = sys.argv

    if len(argz) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    fp = argz[1]
    t = count_book_words(fp)
    s = count_book_chars_list(fp)
    s.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print(F"Analyzing book found at {fp}")
    print("---------- Word Count ----------")
    print(f"Found {t} total words")
    print("-------- Character Count --------")
    for u in s:
        print(f"{u["name"]}: {u["num"]}")

main()