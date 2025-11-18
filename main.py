from stats import word_counter as WC, charaCounter as CC
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    path = "/home/chris/bootdev/github/bookbot/bookbot/books/frankenstein.txt"
    print(get_book_text(path))

def word_counter2(booktext):
    split_lines = booktext.split()
    arr = []
    for line in split_lines:
        arr+=line.split()
    func = lambda word: word != ""
    arr2 = list(filter(func, arr))
    print(arr2)

def CCPrinter(dct):
    printText = ""
    for x in dct:
        printText += f"{x}: {dct[x]}\n"
    return printText

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    pass

bookpath = sys.argv[1]
bookText = get_book_text(bookpath)
CCdict = CC(bookText)

finalOutput = f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
{WC(get_book_text(bookpath))}
--------- Character Count -------
{CCPrinter(CCdict)}
============= END ===============
"""
print(finalOutput)
