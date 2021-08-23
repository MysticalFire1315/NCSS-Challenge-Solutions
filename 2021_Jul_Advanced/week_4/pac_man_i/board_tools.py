def find_on_board(board, item):
  """
  Find the locations of items on a board.
  
  :param maze: The board.
  :type maze: list
  
  :param item: The item to find.
  :type item: str
  
  :return: A list of coordinates where items are located. Format (X, Y).
  :rtype: list
  """
  # Initialise an empty list to store item locations
  items = []
  
  # Loop through every square in maze
  for column in range(len(board)):
    for row in range(len(board[column])):
      # Check if square is a item
      if board[column][row] == item:
        # Append to list of item locations
        items.append(tuple([column, row]))
  
  # Return item locations
  return items

def parse_board_from_file(board_file_name, invert=False):
  """
  Parse a file containing a 2D board. Returns an array of board rows as strings.
  
  :param board_file_name: The name of the file to get board from.
  :type board_file_name: str
  
  :return: An array representation of the board.
  :rtype: list
  """
  board = []
  for line in open(board_file_name, 'r'):
    board.append(line.strip())
  
  # If invert is true, convert rows to columns
  if invert is True:
    return rows_to_columns(board)
  return board

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