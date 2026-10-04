def count_words(book_text: str) -> int:
  word_list = book_text.split()
  word_count = len(word_list)
  return word_count


def count_chars(book_text: str) -> dict[str, int]:
  char_count: dict[str, int] = {}

  for char in book_text:
    lowered_char = char.lower()

    if lowered_char in char_count:
      char_count[lowered_char] += 1
    else:
      char_count[lowered_char] = 1

  return char_count
