from numpy.polynomial import Polynomial as P
# More about numpy's polynomial classes at:
#   https://numpy.org/doc/stable/reference/routines.polynomials.classes.html

OPERATORS = ('+', '-', '*', '^')

def parse(rpn):
  """
  Parses a string of RPN.
  
  :param rpn: The RPN formatted string.
  :type rpn: str
  
  :return: A :class:`numpy.polynomial.Polynomial` object.
  :rtype: :class:`numpy.polynomial.Polynomial`
  """
  # Initialise stack
  stack = []
  # Set default pronumeral as x
  pronumeral = 'x'
  
  # Loop through each character
  for character in rpn.split():
    # Check if character is an operator
    if character in OPERATORS:
      # Pop last two items off stack
      term1 = stack.pop(-2)
      term2 = stack.pop(-1)
      
      # Apply operations as needed and append result to stack
      if character == OPERATORS[0]:
        stack.append(term1 + term2)
        
      elif character == OPERATORS[1]:
        stack.append(term1 - term2)
        
      elif character == OPERATORS[2]:
        stack.append(term1 * term2)
        
      elif character == OPERATORS[3]:
        # Here a Polynomial can only be raised to a power of an integer
        stack.append(term1 ** term2.coef[0])
    
    else:
      # If not an operator, try as an integer
      try:
        # Append polynomial as integer to stack
        stack.append(P([int(character)]))
      except:
        # Append polynomial as just pronumeral to stack and set pronumeral
        pronumeral = character
        stack.append(P([0, 1]))
  
  # Return stack and pronumeral
  return stack, pronumeral