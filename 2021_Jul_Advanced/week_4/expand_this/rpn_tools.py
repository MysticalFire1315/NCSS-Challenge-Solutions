# Not used
from polynomial import Polynomial, Term

class Parser:
  """
  RPN parser object.
  """
  
  OPERATORS = ['+', '-', '*', '^']
  
  def __init__(self, rpn=None):
    self._rpn = rpn
    
  def parse(self, rpn=None):
    """
    Parse a RPN format string.
    
    :param rpn: The RPN string to parse.
    :type rpn: str
    
    :return: 
    """
    # Input parameter type checking
    if rpn is None:
      # Get instance's RPN
      if self._rpn is None:
        # If also None raise error
        raise TypeError
      
      # Otherwise set to instance's rpn
      rpn = self._rpn
    
    # Strip trailing newline and split at whitespace
    rpn = rpn.strip().split()
    
    pronumeral = None
    
    # Check that there is only one pronumeral
    for character in rpn:
      try:
        int(character)
      except:
        if character not in self.OPERATORS:
          if pronumeral is not None and character != pronumeral:
            raise ValueError
          else:
            pronumeral = character
            
    if pronumeral is None:
      pronumeral = 'x'
    
    # Create a stack to store operations
    stack = []
    
    # Loop through each character
    for character in rpn:
      # Check if character is an operator
      if character in self.OPERATORS:
        # Pop top two off stack
        term2 = stack.pop(-1)
        term1 = stack.pop(-1)
        
        if character == self.OPERATORS[0]:
          stack.append(term1+term2)
        elif character == self.OPERATORS[1]:
          stack.append(term1-term2)
        elif character == self.OPERATORS[2]:
          stack.append(term1*term2)
        elif character == self.OPERATORS[3]:
          stack.append(term1**term2)
      
      else:
        # Try converting character into an integer
          
        try:
          # Push integer term to stack
          stack.append(Polynomial([Term(int(character), pronumeral, 0)], pronumeral))
        except:
          # If cannot convert to integer, treat as pronumeral
          stack.append(Polynomial([Term(1, pronumeral, power=1)], pronumeral))
    
    return stack
