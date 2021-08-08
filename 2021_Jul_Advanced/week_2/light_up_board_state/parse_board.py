# Constants that represent what the cell is
WHITE = '.'
BLACK_UNNUMBERED = 'X'
BLACK_NUMBERED = ['0', '1', '2', '3', '4']
LAMP = 'L'
ILLUMINATED = 'Y'

def rows_to_columns(board):
  """
  Convert a board where each subarray represents a row to a board where each
  subarray represents a column.
  
  :param board: The board where each subarray represents a row.
  :type board: arr
  
  :return: The board where each subarray represents a column.
  :type board: arr
  """
  # Initialise array to store reformatted board
  reformatted_board = []
  # Loop through to get each column of each row to store in reformatted board
  for index in range(len(board[0])):
    # Get column
    column = []
    for row in board:
      column.append(row[index])
    # Add column to reformatted board
    reformatted_board.append(''.join(column))
  return reformatted_board