#! 5 min 57 sec
#! #1 passed all tests

def to_camel(ident):
  # TODO implement this function.
  # Check if underscore (_) in ident
  copied = ""
  if "_" in ident:
    # Loop through characters
    was_underscore = False
    for index in range(len(ident)):
      # Check if character before was underscore
      if was_underscore is True:
        copied += ident[index].upper()
        was_underscore = False
      elif ident[index] == "_":
        was_underscore = True
      else:
        copied += ident[index]
  else:
    copied = ident
  return copied


if __name__ == '__main__':
  # Run the example inputs in the question.
  print(to_camel('foo'))
  print(to_camel('raw_input'))
  print(to_camel('num2words'))
  print(to_camel('num_to_SMS'))