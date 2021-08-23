#! 34 min 14 sec
#! #1

#! Execution time (Example 1): 0.0008919559986679815
#! Execution time (Example 2): 0.0007767200004309416
#! Execution time (Size=100, Moves=10, Knight=20,30): 0.07599215699883644

from chess_pieces import Knight
from utils import array_max, is_populated, rows_to_columns

from time import perf_counter

def the_cover_of_knight():
  size = int(input('Size: '))
  max_moves = int(input('Moves: '))
  knight_pos = input('Knight: ')
  
  start_time = perf_counter()
  
  knight_pos = [int(coordinate) for coordinate in knight_pos.split(',')]
  # Board works with X as horizontal and Y as vertical
  knight_pos = knight_pos[::-1]
  
  # Get board
  board = recursive_moves(
    # First plot moves of knight's original position onto a new board
    plot_moves(build_board(size), [knight_pos], '0'),
    max_moves,
    # What the board looks like doesn't really matter
    [Knight(build_board(size), knight_pos)]
  )
  
  # Display
  for row in rows_to_columns(board):
    print(' '.join(row))
  
  end_time = perf_counter()
  print(end_time - start_time)

def recursive_moves(board, max_moves, pieces, depth=1):
  """
  Recursively identify and plot moves. Recurses until either max moves is
  reached or board is entirely populated (all squares have been moved to at
  least once).
  
  :param board: The board.
  :type board: list
  
  :param max_moves: The maximum number of moves.
  :type max_moves: int
  
  :param pieces: An array of Knight pieces.
  :type piece: :class:`Knight`
  
  :return: The populated board.
  :rtype: list
  """
  # First check if conditions are met => Exit recursion if met
  if depth > max_moves:
    return board
  elif is_populated(board):
    return board
  
  # Get possible moves
  possible_moves = []
  # Loop through knight pieces to find possible moves for each piece
  for knight in pieces:
    # Get moves for each piece
    for piece_move in knight.get_moves():
      # To avoid duplication of a move, check if it's already been identified
      # either in this depth or a previous level
      if (board[piece_move[0]][piece_move[1]] == '.' and
          piece_move not in possible_moves):
        possible_moves.append(piece_move)
  
  # Create an array of Knight pieces for each move identified
  pieces = []
  for move in possible_moves:
    pieces.append(Knight(board, move))
  
  # Recurse
  return recursive_moves(
    # Plot moves of current depth's positions
    plot_moves(board, possible_moves, str(int(array_max(board))+1)),
    max_moves, pieces, depth=depth+1)

def plot_moves(board, moves, char):
  """
  Plot the moves.
  
  :param board: The board to plot moves on.
  :type board: list
  
  :param moves: An array containing subarrays of move coordinates to plot.
  :type moves: list
  
  :param char: The character used to plot the moves.
  :type char: str
  
  :return: The board with all moves plotted.
  :rtype: list
  """
  for x, y in moves:
    if board[x][y] == '.':
      board[x][y] = char
  return board

def build_board(size):
  """
  A board must be square, so size determines the dimensions.
  
  :param size: An integer representation of the number of squares in each row.
  :type size: int
  
  :return: The board as an array with each subarray representing a row.
  :rtype: list
  """
  # Create board
  return [['.' for y in range(size)] for x in range(size)]

if __name__ == '__main__':
  the_cover_of_knight()