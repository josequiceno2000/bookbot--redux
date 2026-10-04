
def get_book_text(file_path: str) -> str:
  with open(file_path) as f:
    file_contents = f.read()
    return file_contents

def count_words(book_text: str) -> int:
  word_list = book_text.split()
  word_count = len(word_list)
  return word_count

def main():
  book_text = get_book_text("books/frankenstein.txt")
  word_count

main()