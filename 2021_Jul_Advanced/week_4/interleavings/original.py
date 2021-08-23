# Original Algorithm
# Uses `itertools.permutation` => MemoryError when strings are too long

from itertools import permutations

def interleavings(a, b):
  # TODO Implement this.
  # First get perms for the two strings concatenated together
  # This meets criteria that all characters in `a` and `b` appear once
  perms = list(permutations(a+b))
  
  # Now we need to remove all perms where order of letters in `a` with
  # respect to each other are not preserved
  perms = check_order(perms, a)
  
  # And do the same for letters in `b`
  perms = check_order(perms, b)
  
  concatenated = []
  # Concatenate perms
  for index in range(len(perms)):
    concatenated.append(''.join(perms[index]))
  
  return sorted(concatenated)

def check_order(to_check, order):
  """
  Check a list and remove any elements where the order does not match the
  order provided.
  
  :param to_check: A list of strings.
  :type to_check: list
  
  :param order: A string containing the order of letters.
  :type order: str
  
  :return: The list of strings with any strings that don't match the given order
           removed.
  :rtype: list
  """
  index_to_remove = []
  # Loop through each element in the list to check
  for i, element in enumerate(to_check):
    current_order = ''
    # Loop through letters to extract letters in the order to match
    for index in range(len(element)):
      if element[index] in order:
        current_order += element[index]
    
    # Check if extracted letters matches the order
    if current_order != order:
      index_to_remove.append(i)
  
  # Remove index
  return removed(to_check, index_to_remove)

def removed(list_to_remove, index_to_remove):
  """
  Remove a list of index from a list of items.
  
  :param list_to_remove: The list to remove items from.
  :type list_to_remove: list
  
  :param index_to_remove: The list of index for items to be removed from.
  :type index_to_remove: list
  
  :return: A list where the items at given index are removed.
  :rtype: list
  """
  # First sort indexes reversed
  for index in sorted(index_to_remove, reverse=True):
    # Remove indexes (start from back to avoid removing items not intended)
    list_to_remove.pop(index)
  return list_to_remove


if __name__ == '__main__':
  # Run the examples in the question.
  result = interleavings('ab', 'cd')
  print(result)
  result = interleavings('a', 'cd')
  print(result)