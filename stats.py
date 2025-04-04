def get_num_words(string):
  array = string.split()
  num_words = len(array)
  return num_words, f"{num_words} words found in the document"

def count_characters(string):
  chars = {}
  for char in string:
    if not char in chars:
      chars[char] = 1
    else:
      chars[char] += 1
  return chars