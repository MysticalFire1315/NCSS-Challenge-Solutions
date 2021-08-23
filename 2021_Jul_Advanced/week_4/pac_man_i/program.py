#! 1hr 8 min 51 sec
#! #1 0 tests passed (Forgot to comment out testing example 2)
#! #2 passed all tests

from board_tools import parse_board_from_file, find_on_board
from pathfinding import breadth_first_search

def pac_man_i(maze_file_name):
  # Get maze, columns as elements in array
  maze = parse_board_from_file(maze_file_name)
  
  # Find ghosts and their locations
  ghosts = find_on_board(maze, 'G')
  # Find pacman
  pacman = find_on_board(maze, 'P')

  # Loop through ghosts to move individually
  ghost_paths = []
  for ghost in ghosts:
    ghost_paths.append(breadth_first_search(maze, ghost, pacman[0]))
  
  board = move_ghosts(maze, ghost_paths)
  for row in board:
    print(row)

def move_ghosts(board, ghost_paths):
  new_board = []
  ghost_position = [path[0] for path in ghost_paths]
  ghost_moves = [path[1] for path in ghost_paths]
  
  for row in range(len(board)):
    current_row = ''
    for column in range(len(board[row])):
      # Check if the square is where any of those currently is
      if tuple([row, column]) in ghost_position:
        current_row += ' '
      elif tuple([row, column]) in ghost_moves:
        current_row += 'G'
      else:
        current_row += board[row][column]
    new_board.append(current_row)
  return new_board

if __name__ == '__main__':
  pac_man_i('maze.txt')
  #pac_man_i('example2.txt')