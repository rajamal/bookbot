import sys
from stats import get_num_words, get_char_counts, get_char_count_list

def get_book_text(file_path):
  with open(file_path) as f:
    file_contents = f.read()
  return file_contents


def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  frankenstein = get_book_text(sys.argv[1])
  frankenstein_words = get_num_words(frankenstein)
  print(f"Found {frankenstein_words} total words")
  char_count_list = get_char_count_list(get_char_counts(frankenstein))
  for d in char_count_list:
    if d["char"].isalpha():
      print(f'{d["char"]}: {d["num"]}')

main()

