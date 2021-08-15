#! 13 min 20 sec
#! #1 passed all tests

# Set alien digits constant
ALIEN_DIGITS = {'a': 0,
                'e': 1,
                'i': 2,
                'o': 3,
                'u': 4}

def alien2float(string):
  # TODO
  # Define a flag to indicate whether the fractional part has been reached
  fraction = False

  # Initialise variables to store integer and fractional parts
  integer = ''
  fractional = ''

  # Split the string into integer and fractional parts
  for index in range(len(string)):
    # Check if character is in uppercase (int part), in alien digits and
    # fractional part has not been reached
    if (string[index] in ''.join(ALIEN_DIGITS.keys()).upper()
        and fraction is False):
      # Add character (in lowercase) to integer part
      integer += string[index].lower()
    
    # Check if character is in lowercase
    elif string[index] in ''.join(ALIEN_DIGITS.keys()):
      # Add character to fractional part
      fractional += string[index]
      # Also set flag to True
      fraction = True
    
    # If either condition is not met, return None
    else:
      return None
  
  # Initialise a variable to store converted string
  return_float = 0.0

  # Work with fractional components first
  # range() function stops at the number before the second parameter, so
  # that has to be set to -1 since we need index 0
  for index in range(len(fractional)-1, -1, -1):
    return_float += ALIEN_DIGITS[fractional[index]] * 5**(-1-index)
  
  # Reverse integer components to make it easier to work with
  integer = integer[::-1]
  for index in range(len(integer)):
    return_float += ALIEN_DIGITS[integer[index].lower()] * 5**index
  
  return return_float

if __name__ == "__main__":
  # Run the examples in the question.
  print(repr(alien2float('IUae')))
  print(repr(alien2float('OUAooea')))
  print(repr(alien2float('iuAE')))