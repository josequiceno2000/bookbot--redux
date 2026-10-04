def sort_on(char_tuple: tuple[str, int]) -> int:
  return char_tuple[1]

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

def chars_dict_to_sorted_list(char_count: dict[str, int]) -> list[tuple[str, int]]:
  chars_tuples: list[tuple[str, int]] = []

  for char, count in char_count.items():
    chars_tuples.append((char, count))

  sorted_chars = sorted(chars_tuples, reverse=True, key=sort_on)

  return sorted_chars