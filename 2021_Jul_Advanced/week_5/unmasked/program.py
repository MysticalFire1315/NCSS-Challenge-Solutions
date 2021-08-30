#! 23 min 12 sec
#! #1 passed all tests

from math import sqrt
from string import punctuation
from utils import (read_into_array, read_into_string,
                   reverse_dict_key_value_pairs)

def unmasked():
  # Get filenames
  filenames = read_into_array('texts.txt')
  
  # Initialise dictionary to store texts
  texts = {}
  
  # Calculate word length frequency for unknown.txt
  unknown_text_freq = word_length_frequency(read_into_string('unknown.txt'))
  
  for text in filenames:
    # Calculate word length frequency for text
    text_word_len_freq = word_length_frequency(read_into_string(text))
    # Calculate and store cosine similarity between unknown and current text
    texts[text] = cosine_similarity(unknown_text_freq, text_word_len_freq)
  
  texts = reverse_dict_key_value_pairs(texts)
  
  for cosine_sim in sorted(texts.keys(), reverse=True):
    for text in texts[cosine_sim]:
      print(f'{cosine_sim} {text}')

def cosine_similarity(dict1, dict2):
  """
  Calculate the cosine similarity between two dictionary objects. Note that keys
  and values of the dictionary objects must be integers.
  
  :param dict1: The first dictionary.
  :type dict1: dict
  
  :param dict2: The second dictionary.
  :type dict2: dict
  
  :return: The cosine similarity.
  :rtype: float
  """
  # Find the largest value in keys
  if max(dict1.keys()) > max(dict2.keys()):
    max_range = max(dict1.keys())
  else:
    max_range = max(dict2.keys())
  
  # Initialise top and bottom parts
  top = 0
  bottom_a = 0
  bottom_b = 0
  
  
  for index in range(max_range+1):
    # Reset current top
    current_top = 0
    
    # Check if value exists in first dict
    if index in dict1.keys():
      # Change current top
      current_top = dict1[index]
      # Add square to bottom
      bottom_a += dict1[index] ** 2
      
    # Check if value exists in second dict
    if index in dict2.keys():
      # Multiply current top
      current_top *= dict2[index]
      # Add square to bottom
      bottom_b += dict2[index] ** 2
    else:
      # Reset current top (multiplication by 0 gives 0)
      current_top = 0
    
    # Sum top
    top += current_top
  
  # Calculate and return fraction
  return top / (sqrt(bottom_a) * sqrt(bottom_b))

def word_length_frequency(string):
  """
  Calculate the frequency of all word lengths in a string.
  
  :param string: The string to examine.
  :type string: str
  
  :return: A dictionary with keys corresponding the word length and values
           corresponding to the frequency it occurs.
  :rtype: dict
  """
  word_len_freq = {}
  for word in string.split():
    # Strip punctuation from word
    word = word.strip(punctuation)
    
    if word:
      # Check if word length has already been seen
      if len(word) in word_len_freq:
        word_len_freq[len(word)] += 1
      else:
        word_len_freq[len(word)] = 1
  return word_len_freq


if __name__ == '__main__':
  unmasked()