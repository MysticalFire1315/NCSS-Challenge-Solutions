#! 4 min 23 sec
#! #1 passed all tests

# Define vowels
VOWELS = ['a', 'e', 'i', 'o', 'u']

def remove_vowels(item):
  new_item = ""
  for index in range(len(item)):
    if item[index].lower() not in VOWELS:
      new_item += item[index]
  return new_item

def novowelsort(the_list):
  # TODO perform no vowel sort on `the_list`.
  # Sort where each item has vowel removed
  the_list.sort(key = lambda item: remove_vowels(item))
  return the_list


if __name__ == '__main__':
  # Example calls to your function.
  print(novowelsort(['alpha', 'beta']))
  print(novowelsort(['once', 'upon', 'abc', 'time', 'there', 'were', 'some', 'words']))