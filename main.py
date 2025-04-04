from stats import get_num_words, count_characters
import sys

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents

def print_report(filepath, words, chars):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {filepath}")
  print("----------- Word Count ----------")
  print(f"Found {words} total words")
  print("--------- Character Count -------")
  for k in chars:
    if k != "":
      print(f"{k}: {chars[k]}")
  print("============= END ===============")

def main():
  args = sys.argv
  if len(args) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    filepath = args[1]
    book = get_book_text(filepath)
    words, message = get_num_words(book)
    chars = count_characters(book.lower())
    print_report(filepath, words, chars)

main()