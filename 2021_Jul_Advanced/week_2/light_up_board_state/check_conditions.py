from parse_board import (rows_to_columns, WHITE, BLACK_UNNUMBERED,
                         BLACK_NUMBERED, LAMP, ILLUMINATED)

def check_line_of_sight(board):
  """
  Check that no two lamps are in NSEW line-of-sight of each other.
  
  :param board: The board to check.
  :type board: arr
  
  :return: A boolean indicator of whether there are lamps in NSEW line-of-sight.
           True indicates that there are lamps in line-of-sight; False indicates
           none in line-of-sight.
  :rtype: bool
  """
  # Check line-of-sight in each row first
  if line_of_sight(board):
    return True
  # Check line-of-sight in each column
  if line_of_sight(rows_to_columns(board)):
    return True
  # Condition met
  return False

def line_of_sight(board):
  """
  Check that no two lamps in each row are in line-of-sight of each other.
  
  :param board: The board to check.
  :type board: arr
  
  :return: A boolean indicator of whether there are lamps in line-of-sight in
           each row. True indicates that there are lamps in line-of-sight; False
           indicates none in line-of-sight.
  :rtype: bool
  """
  
  for row in board:
    # Sight variable indicates that there is a lamp in line of sight
    sight = False # Start at false for each row
    
    for index in range(len(row)):
      # Check if cell is a lamp
      if row[index] == LAMP:
        # Check if there is a lamp in line of sight
        if not sight:
          # No lamp in sight, so set sight to true
          sight = True
        else:
          # There is a lamp in sight, so condition already not met
          return True
      
      # Check if cell is a black cell
      if row[index] == BLACK_UNNUMBERED or row[index] in BLACK_NUMBERED:
        # Black cells block line of sight
        sight = False
  
  # No lamps in line of sight on each row
  return False

def check_numbered_adjacent_less_or_equal(board):
  """
  Check that the number of adjacent lamps to each black square is less than or
  equal to the number in the black square (if numbered).
  
  :param board: The board to check.
  :type board: arr
  
  :return: A boolean indicator of whether the number of lamps adjacent to each
           black square is less than or equal to the number in the square. True
           indicates that the condition is met; False indicates that there are
           more than the number in the square.
  :rtype: bool
  """
  # Loop through each row in board
  for row in range(len(board)):
    # Loop through each column in row
    for column in range(len(board[row])):
      # Check if cell is a numbered black cell
      if board[row][column] in BLACK_NUMBERED:
        # Convert the number to an int
        max_lamps = int(board[row][column])
        
        # Try looking directly above
        try:
          # If cell directly above is a lamp
          if board[row-1][column] == LAMP:
            max_lamps -= 1
        except:
          pass
        
        # Try looking directly below
        try:
          # If cell directly below is a lamp
          if board[row+1][column] == LAMP:
            max_lamps -= 1
        except:
          pass
        
        # Try looking directly left
        try:
          # If cell directly left is a lamp
          if board[row][column-1] == LAMP:
            max_lamps -= 1
        except:
          pass
        
        # Try looking directly right
        try:
          # If cell directly right is a lamp
          if board[row][column+1] == LAMP:
            max_lamps -= 1
        except:
          pass
        
        # Check that the max amount of lamps is not negative
        # max_lamps < 0 means that the number of adjacent lamps has exceeded
        # the number on the cell, which also means condition has not been met
        if max_lamps < 0:
          return False
  return True

def check_numbered_adjacent_exact(board):
  """
  Check that the number of adjacent lamps to each black square is equal to the
  number in the black square (if numbered).
  
  :param board: The board to check.
  :type board: arr
  
  :return: A boolean indicator of whether the number of lamps adjacent to each
           black square is equal to the number in the square. True indicates
           that the condition is met; False indicates that there are more or
           less than the number in the square.
  :rtype: bool
  """
  # Loop through each row in board
  for row in range(len(board)):
    # Loop through each column in row
    for column in range(len(board[row])):
      # Check if cell is a numbered black cell
      if board[row][column] in BLACK_NUMBERED:
        # Convert the number to an int
        max_lamps = int(board[row][column])
        
        # Try looking directly above
        try:
          # If cell directly above is a lamp
          if board[row-1][column] == LAMP:
            max_lamps -= 1
        except:
          pass
        
        # Try looking directly below
        try:
          # If cell directly below is a lamp
          if board[row+1][column] == LAMP:
            max_lamps -= 1
        except:
          pass
        
        # Try looking directly left
        try:
          # If cell directly left is a lamp
          if board[row][column-1] == LAMP:
            max_lamps -= 1
        except:
          pass
        
        # Try looking directly right
        try:
          # If cell directly right is a lamp
          if board[row][column+1] == LAMP:
            max_lamps -= 1
        except:
          pass
        
        # Check that the max amount of lamps is 0
        # max_lamps not 0 means that the number of adjacent lamps is either more
        # or less than the number, which also means condition has not been met
        if max_lamps != 0:
          return False
  return True

def check_all_white_illuminated(board):
  """
  Check that all white squares have been illuminated.
  
  :param board: The board to check.
  :type board: arr
  
  :return: A boolean indicator of whether all light squares have been
           illuminated. True indicates that all squares are illuminated; False
           indicates that there are white squares not illuminated.
  :rtype: bool
  """
  # Illuminate white squares in each row first
  board = illuminate_rows(board)
  # Illuminate white squares in each column
  board = illuminate_rows(rows_to_columns(board))
  
  # Check if there are still any white squares in the board
  for row in range(len(board)):
    for column in range(len(board[row])):
      # Check if cell is a white square
      if board[row][column] == WHITE:
        # If there are still white squares left, that means not all squares
        # have been illuminated, and condition is not met
        return False
  # Condition met
  return True

def illuminate_rows(board):
  """
  Illuminate all white squares in each row if there are lamps.
  
  :param board: The board to illuminate white squares in.
  :type board: arr
  
  :return: The board with all illuminated squares as Y.
  :rtype: arr
  """
  # Loop through each row in board
  for row in range(len(board)):
    # Sight variable indicates there is a lamp in line of sight
    sight = False
    
    # Initialise a string to store row after conversion
    converted_row = ""
    
    # Loop through each column in row
    for column in range(len(board[row])):
      # Check if cell is a lamp cell
      if board[row][column] == LAMP:
        sight = True
        converted_row += board[row][column]
      
      # Check if cell is a black cell
      if (board[row][column] == BLACK_UNNUMBERED
          or board[row][column] in BLACK_NUMBERED):
        # Black cells block line of sight
        sight = False
        converted_row += board[row][column]
      
      # Check if cell is a white cell
      if board[row][column] == WHITE:
        # Check if lamp in line of sight
        if sight is True:
          # If lamp in line of sight, change white square to Y
          converted_row += 'Y'
        else:
          converted_row += board[row][column]
    
    # Change board row to converted row reversed and reset converted row
    board[row] = converted_row[::-1]
    converted_row = ""
    
    sight = False
    
    # Loop through each column in row
    for column in range(len(board[row])):
      # Check if cell is a lamp cell
      if board[row][column] == LAMP:
        sight = True
        converted_row += board[row][column]
      
      # Check if cell is a black cell
      if (board[row][column] == BLACK_UNNUMBERED
          or board[row][column] in BLACK_NUMBERED):
        # Black cells block line of sight
        sight = False
        converted_row += board[row][column]
      
      # Check if cell is already illuminated
      if board[row][column] == ILLUMINATED:
        converted_row += board[row][column]
      
      # Check if cell is a white cell
      if board[row][column] == WHITE:
        # Check if lamp in line of sight
        if sight is True:
          # If lamp in line of sight, change white square to Y
          converted_row += 'Y'
        else:
          converted_row += board[row][column]
    
    # Change board row to converted row reversed (back to original orientation)
    board[row] = converted_row[::-1]
  
  return board