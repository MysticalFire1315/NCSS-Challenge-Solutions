#! 3 hr 24 min 42 sec
#! #1 4 tests passed (reordered replace statements so trailing 1 isn't cut)
#! #2 6 tests passed (shows trailing 0)
#! #3 13 tests passed (error raised in display if length is < 3)
#! #4 13 tests passed (error raised in display if polynomial is 0)
#! #5 passed all tests (redid everything using Numpy's Polynomial class)

from rpn_numpy import parse

def expand_this():
  # Get inputs
  rpn = input('RPN: ')
  
  # Parse RPN
  parsed = parse(rpn)
  
  # Get equation and polynomials
  equation = parsed[0][0]
  pronumeral = parsed[1]
  
  # Initialise an array to store items to print
  to_print = []
  # Loop through each coefficient
  for index in range(len(equation.coef)):
    # Check if coefficient is 0
    if equation.coef[index] != 0:
      # Check index (which is power)
      if index == 0:
        # If 0, then just show the coefficient
        to_print.append(f'{int(equation.coef[index])}')
      elif index == 1:
        # If 1, then just show coefficient and x
        to_print.append(f'{int(equation.coef[index])}{pronumeral}')
      else:
        # Otherwise add everything for display
        to_print.append(f'{int(equation.coef[index])}{pronumeral}^{index}')
    
    # If length is 1 (ie. just an integer)
    elif len(equation) == 1:
      # Just display 0
      to_print.append('0')
    # Otherwise do nothing
  
  # Join everything to display
  to_print = ' + '.join(to_print[::-1]).replace('+ -', '- ')
  print(to_print.replace('1'+pronumeral, pronumeral))

if __name__ == '__main__':
  expand_this()