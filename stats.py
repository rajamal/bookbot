def get_num_words(text):
  return len(text.split())

def get_char_counts(text):
  counter = {}
  for ch in text.lower():
    if ch in counter:
      counter[ch] += 1
    else:
      counter[ch] = 1

  return counter

def get_char_count_list(char_counts):
  count_list = []
  for ch, count in char_counts.items():
    count_list.append({"char": ch, "num": count})

  count_list.sort(reverse=True, key=lambda x: x["num"])
  return count_list

