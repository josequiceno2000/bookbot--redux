
from stats import count_words, count_chars, chars_dict_to_sorted_list

def get_book_text(file_path: str) -> str:
  with open(file_path) as f:
    file_contents = f.read()
    return file_contents
  
def main():
  book_text = get_book_text("books/frankenstein.txt")
  word_count = count_words(book_text)
  char_count = count_chars(book_text)
  sorted_chars = chars_dict_to_sorted_list(char_count)
  print(f"Found {word_count} total words")
  print(sorted_chars)

main()