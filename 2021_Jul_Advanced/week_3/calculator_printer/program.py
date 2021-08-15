#! 35 min 17 sec
#! #1 0 tests passed (7 had extra top left bar => like in picture)
#! #2 passed all tests

from templates import seven_segment_display_template

def calculator_printer():
  # Get inputs
  number = input('Number: ')
  width = int(input('Width: '))

  # Start by creating an array to store each row
  rows = []

  # There are a minimum of 5 rows, so loop through 5 times
  for i in range(5):
    # Initialise a string to store the row in
    row = ''

    # Loop through each digit in the number
    for digit in number:
      row += f'{seven_segment_display_template[int(digit)][i]} '
    
    # Get rid of the excess space at the end
    row = row[:-1]

    # Replace any dashes and spaces with the necessary number
    rows.append(row.replace('dash', '-'*width).replace('space', ' '*width))
  
  # Initialise a string to store the final display
  display = ''

  for index in range(5):
    # Only repeat rows 2 and 4 (index 1 & 3)
    if index == 1 or index == 3:
      # Loop through number of columns
      for i in range(width):
        display += f'{rows[index]}\n'
    else:
      display += f'{rows[index]}\n'
  
  # Print display without trailing newline character
  print(display[:-1])


if __name__ == '__main__':
  calculator_printer()