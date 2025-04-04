def get_num_words(string):
  array = string.split()
  num_words = len(array)
  return num_words, f"{num_words} words found in the document"