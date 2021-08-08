#! 45 min 56 sec
#! #1 passed all tests

import random
from ml_models import MarkovModel

# Define max length of sentence
MAX_SENTENCE_LENGTH = 200

def generate_sentence(start_token, filenames):
  # TODO
  
  # Create string to store all file contents in
  all_text = []
  
  # Loop through files to add contents to a single string
  for filename in filenames:
    # Loop through lines in file to remove paragraph breaks and trailing
    # newline characters
    text = ""
    for line in open(filename, "r"):
      # Check if line is a paragraph break (ie newline)
      if line != "\n":
        text += line.strip() + " "
    
    # Files are disjoint, so add text from file into all text array
    all_text.append(text)
  
  # Create instance of MarkovModel
  model = MarkovModel()
  # Fit all text to model
  model.fit(all_text)
  
  # Initialise array to store sentence
  sentence = [start_token.lower()]
  
  # Check conditions were not met
  while conditions(sentence, model.model, MAX_SENTENCE_LENGTH) is False:
    # Get random token to add to sentence
    sentence.append(random.choice(model.model[sentence[-1]]))
  
  return " ".join(sentence)

def conditions(sentence, model, max_length):
  # Check conditions
  # 1. the previously generated token was a full stop
  if sentence[-1] == ".":
    return True
  # 2. there is no next possible token
  elif len(model[sentence[-1]]) <= 0:
    return True
  # 3. or the produced sentence is 200 tokens in length
  elif len(sentence) >=  max_length:
    return True
  
  # Conditions not met
  return False

if __name__ == '__main__':
  # The random number generator is initialised to zero here purely
  # for your own testing so that each time you run your code during
  # development, you will get the same output. Remove this to get 
  # different output each time you run your code with the same input.
  random.seed(0)
  
  # Run the examples in the question.
  for i in range(4):
    print(generate_sentence('There', ['single.txt']))
  print('=' * 80)
  for i in range(4):
    print(generate_sentence('the', ['jab.txt']))
  print('=' * 80)
  for i in range(4):
    print(generate_sentence('It', ['dracula.txt', 'pandp.txt']))
  print('=' * 80)
  for i in range(10):
    print(generate_sentence('Once', ['dracula.txt', 'jb.txt', 'pandp.txt', 'totc.txt']))
  print('=' * 80)
  for i in range(8):
    print(generate_sentence('cat', ['single.txt', 'textwraps.txt']))
  print('=' * 80)