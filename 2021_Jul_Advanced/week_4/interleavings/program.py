#! 19 min 56 sec
#! #1 6 tests passed (using itertools.permutations => MemoryError with long str)
#! #2 passed all tests

def interleavings(a, b):
  # TODO Implement this.
  return interleave(a, b)

def interleave(a, b, prefix=''):
  """
  Take first character of two strings `a` and `b` and add to `prefix`.
  
  :param a: The first string.
  :type a: str
  
  :param b: The second string.
  :type b: str
  
  :param prefix: The current string to attach characters to. (Defaults to '')
  :type prefix: str
  
  :return: A list containing the prefix with either character attached.
  :rtype: list
  """
  if not a:
    # If a is empty, list will only have b and whatever prefix was
    return [prefix + b]
  if not b:
    # If b is empty, list will only have a and whatever prefix was
    return [prefix + a]
  
  # Branch out prefix with letter in 'a'
  prefix_a = interleave(a[1:], b, prefix + a[0])
  
  # Branch out prefix with letter in 'b'
  prefix_b = interleave(a, b[1:], prefix + b[0])
  
  # Combine branches to return
  return sorted(prefix_a + prefix_b)

if __name__ == '__main__':
  # Run the examples in the question.
  print(interleavings('ab', 'cd'))
  print(interleavings('a', 'cd'))
  print(interleavings('abcdef', 'ghij'))