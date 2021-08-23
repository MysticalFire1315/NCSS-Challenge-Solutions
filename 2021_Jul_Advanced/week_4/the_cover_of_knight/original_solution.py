# Original algorithm

#! Execution time (Example 1): 0.0007659319999220315
#! Execution time (Example 2): 0.0012259320064913481
#! Execution time (Size=100, Moves=10, Knight=20,30): 0.3295925089987577

from chess_pieces import Knight
from utils import rows_to_columns

from time import perf_counter

def the_cover_of_knight():
  size = int(input('Size: '))
  max_moves = int(input('Moves: '))
  knight_pos = input('Knight: ')
  
  start_time = perf_counter()
  
  knight_pos = [int(coordinate) for coordinate in knight_pos.split(',')]
  # Board works with X as horizontal and Y as vertical
  knight_pos = knight_pos[::-1]
  
  # Plot Knight's original position
  board = plot_moves(build_board(size), [knight_pos], '0')
  pieces = [Knight(board, knight_pos)]
  
  depth = 1
  while depth <= max_moves:
    possible_moves = []
    for knight in pieces:
      for piece_move in knight.get_moves():
        if piece_move not in possible_moves:
          possible_moves.append(piece_move)
  
    board = plot_moves(board, possible_moves, str(depth))
    
    pieces = []
    for move in possible_moves:
      pieces.append(Knight(board, move))
    
    depth += 1
  
  for row in rows_to_columns(board):
    print(' '.join(row))
  
  end_time = perf_counter()
  print(end_time-start_time)

def plot_moves(board, moves, char):
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