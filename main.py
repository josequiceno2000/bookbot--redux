
import sys
from stats import count_words, count_chars, chars_dict_to_sorted_list

def get_book_text(file_path: str) -> str:
  with open(file_path) as f:
    file_contents = f.read()
    return file_contents

def print_report(book_path: str, word_count: int, sorted_chars: list[tuple[str, int]]) -> None:
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")

  for char_count in sorted_chars:
    letter = char_count[0]
    if letter.isalpha():
      count = char_count[1]
      print(f"{letter}: {count}")

  print("============= END ===============")
  
def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_path = sys.argv[1]
  book_text = get_book_text(book_path)
  word_count = count_words(book_text)
  char_count = count_chars(book_text)
  sorted_chars = chars_dict_to_sorted_list(char_count)
  print_report(book_path, word_count, sorted_chars)

main()