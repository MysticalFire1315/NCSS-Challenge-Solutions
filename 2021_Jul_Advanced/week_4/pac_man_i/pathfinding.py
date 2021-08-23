def breadth_first_search(board, start, end, walls=["#"]):
  """
  Uses a Breadth-First Search (BFS) algorithm to determine the shortest path
  from start to end on a board.
  
  :param board: The board.
  :type board: list
  
  :param start: The start coordinate. (board's column index, board's row index)
  :type start: tuple
  
  :param end: The end coordinate. (board's column index, board's row index)
  :type end: tuple
  
  :param walls: The symbol(s) representing walls, which cannot be passed through.
  :type walls: list
  
  :return: A list representing the shortest path from start to end.
  :rtype: list
  """
  # Start with an empty todo queue with only the start coordinate
  todo = [[start]]
  # Initialise an empty seen queue
  seen = []
  
  # WHLIE todo is not empty
  while todo:
    # Pop first item
    current_path = todo.pop(0)
    
    # Check if current path ends at target destination
    if current_path[-1] == end:
      # Terminate and return current path
      return current_path
    
    # Ensure current path ends somewhere not seen and not a wall
    if current_path[-1] not in seen and current_path[-1] not in walls:
      seen.append(current_path[-1])
      # Take steps in order: up, left, down, right
      
      # Start with up
      # Clone current path
      path = current_path.copy()
      # Identify next square
      next_square = tuple([current_path[-1][0] - 1, current_path[-1][1]])
      if next_square not in seen:
        # Check square hasn't been seen
        try:
          if board[next_square[0]][next_square[1]] not in walls:
            # Check square exists and is not a wall
            path.append(next_square)
            todo.append(path)
        except:
          # Square does not exist, so do nothing
          pass
      
      # Check left
      # Clone current path
      path = current_path.copy()
      # Identify next square
      next_square = tuple([current_path[-1][0], current_path[-1][1] - 1])
      if next_square not in seen:
        # Check square hasn't been seen
        try:
          if board[next_square[0]][next_square[1]] not in walls:
            # Check square exists and is not a wall
            path.append(next_square)
            todo.append(path)
        except:
          # Square does not exist, so do nothing
          pass
      
      # Check down
      # Clone current path
      path = current_path.copy()
      # Identify next square
      next_square = tuple([current_path[-1][0] + 1, current_path[-1][1]])
      if next_square not in seen:
        # Check square hasn't been seen
        try:
          if board[next_square[0]][next_square[1]] not in walls:
            # Check square exists and is not a wall
            path.append(next_square)
            todo.append(path)
        except:
          # Square does not exist, so do nothing
          pass
      
      # Check right
      # Clone current path
      path = current_path.copy()
      # Identify next square
      next_square = tuple([current_path[-1][0], current_path[-1][1] + 1])
      if next_square not in seen:
        # Check square hasn't been seen
        try:
          if board[next_square[0]][next_square[1]] not in walls:
            # Check square exists and is not a wall
            path.append(next_square)
            todo.append(path)
        except:
          # Square does not exist, so do nothing
          pass
  
  raise MemoryError('Path not found')