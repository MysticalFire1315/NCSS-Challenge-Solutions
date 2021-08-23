def exists(array, coordinate):
  """
  Check that a given coordinate exists in the array.
  
  :param array: The array.
  :type array: list
  
  :param coordinate: The coordinate to verify in a list-like form (X, Y).
  :type coordinate: list-like
  
  :return: A boolean to indicate whether the coordinate exists.
  :rtype: bool
  """
  if coordinate[0] < 0 or coordinate[0] >= len(array):
    return False
  elif coordinate[1] < 0 or coordinate[1] >= len(array[coordinate[0]]):
    return False
  else:
    return True

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
    reformatted_board.append(column)
  return reformatted_board

def array_max(array):
  """
  Find the maximum value in an array.
  
  :param array: The array to look through.
  :type array: list
  
  :return: The maximum value in the array.
  :rtype: any
  """
  try:
    # Set max value as the max in first row
    max_val = max(array[0])
  except:
    # If not possible, raise error
    raise ValueError
  
  for row in array:
    row_max = max(row)
    if row_max > max_val:
      max_val = row_max
      
  return max_val

def is_populated(board):
  """
  Check if a board is populated.
  """
  for x in range(len(board)):
    for y in range(len(board[x])):
      if board[x][y] == '.':
        return False
  return True