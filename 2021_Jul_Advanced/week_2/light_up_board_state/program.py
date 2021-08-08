#! 1hr 2 min 32 sec
#! #1 passed all tests

from check_conditions import (check_line_of_sight,
                              check_numbered_adjacent_less_or_equal,
                              check_numbered_adjacent_exact,
                              check_all_white_illuminated)

def board_is_happy(board):
  """
  Check if board is happy. A board is happy if:
    1. no two lamps are in NSEW (North/South/East/West) line-of-sight of each
       other;
    2. black cells with numbers have less than or equal to that many lamps as
       direct NSEW adjacent neighbours.
  
  :param board: The board to check.
  :type board: arr
  
  :return: A boolean indicator of whether the board is happy. True indicates
           the board is happy; False indicates a condition has not been met.
  :rtype: bool
  """
  # Check condition 1
  if check_line_of_sight(board):
    # Function returns True if there are lamps in line-of-sight
    # This also means that condition 1 has not been met
    return False
  # Check condition 2
  if not check_numbered_adjacent_less_or_equal(board):
    # Executed if number of adjacent lamps to a numbered black cell is not less
    # than or equal to the number on the cell
    # This also means that condition 2 has not been met
    return False
  
  # Conditions met
  return True  # TODO


def board_is_solved(board):
  """ 
  Check if board is solved. A board is solved if:
    1. the board is happy;
    2. all black cells with numbers have *exactly* that many lamps as direct
       NSEW adjacent neighbours;
    3. all white cells are illuminated yellow.
  
  :param board: The board to check.
  :type board: arr
  
  :return: A boolean indicator of whether the board is solved. True indicates
           the board is happy; False indicates a condition has not been met.
  :rtype: bool
  """
  # Check condition 1
  if not board_is_happy(board):
    # Function returns False if board is not happy
    # This also means that condition 1 has not been met
    return False
  # Check condition 2
  if not check_numbered_adjacent_exact(board):
    # Function returns False if a numbered black cell does not have exactly
    # that many adjacent lamps
    # This also means that condition 2 has not been met
    return False
  # Check condition 3
  if not check_all_white_illuminated(board):
    # Function returns False if not all white squares are illuminated
    # This also means that condition 3 has not been met
    return False
  
  # Conditions met
  return True  # TODO


def get_board_state(board):
  if board_is_happy(board):
    if board_is_solved(board):
      return 'solved'
    else:
      return 'happy'
  else:
    return 'unhappy'


if __name__ == '__main__':
  # Example board, happy state.
  print(get_board_state('''
...1.0.
X......
..X.X..
X...L.X
..X.3..
.L....X
L3L2...'''.strip().split('\n')))
  # Example board, solved state.
  print(get_board_state('''
..L1.0.
X...L..
L.X.X.L
X...L.X
..XL3L.
.L....X
L3L2L..'''.strip().split('\n')))
  # Example board, unhappy state.
  print(get_board_state('''
L..1L0.
X.L....
L.X.X.L
X...L.X
..XL3L.
.L....X
L3L2L..'''.strip().split('\n')))
  # Different board, happy state.
  print(get_board_state('''
L1.L.
..L3L
..X1.
.1...
.....'''.strip().split('\n')))