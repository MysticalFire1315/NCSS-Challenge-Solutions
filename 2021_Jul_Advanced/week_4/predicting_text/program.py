#! 40 min 9 sec
#! #1 9 tests passed (Don't need to handle lowercase - this is a separate node)
#! #2 passed all tests

# Implement the following Node class API.
# If you delete something important, this code is copied in specification.py

class Node:
  def __init__(self, prefix):
    """
    Creates a Node with the given string prefix.
    The root node will be given prefix ''.
    You will need to track:
    - the prefix
    - whether this prefix is also a complete word
    - child nodes
    """
    self._prefix = prefix
    self._isword = False
    self._child_nodes = []
  
  def get_prefix(self):
    """
    Returns the string prefix for this node.
    """
    return self._prefix
  
  def get_children(self):
    """
    Returns a list of child Node objects, in any order.
    """
    return self._child_nodes
  
  def debug_children(self):
    """
    Recurses through all children to print their properties.
    """
    # Display current node prefix (`self._prefix` property)
    print(f'\nNode prefix: {self.get_prefix()}')
    # Display whether current node is a word (`self._isword` property)
    print(f'Is Word: {self.is_word()}')
    # Display a list of children node prefixes (`child._prefix` property)
    print(f'Children: {[child.get_prefix() for child in self.get_children()]}')
    
    # Loop through children to call view their properties
    for child in self.get_children():
      child.debug_children()
  
  def is_word(self):
    """
    Returns True if this node prefix is also a complete word.
    """
    return self._isword
  
  def set_word(self):
    """
    Sets this node as a complete word.
    """
    self._isword = True
  
  def add_word(self, word):
    """
    Adds the complete word into the trie, causing child nodes to be created as needed.
    We will only call this method on the root node, e.g.
    >>> root = Node('')
    >>> root.add_word('cheese')
    """
    # Check if word input parameter is empty
    if not word:
      # If it is, that means this node is a word
      self.set_word()
      # Can exit after setting node as word
      return
    
    # Loop through children to find one with prefix that matches the word
    for child_node in self.get_children():
      # Check if last letter of child's prefix matches with first letter of word
      if child_node.get_prefix()[-1] == word[0]:
        # If so, recurse down into child to add word
        child_node.add_word(word[1:])
        # Exit so another identical node isn't accidentally added
        return
    
    # This executes if no current child with the prefix can be found
    # Create a new child node with correct prefix
    child = Node(self.get_prefix() + word[0])
    # Add word
    child.add_word(word[1:])
    # Add child to list of children for current node
    self._child_nodes.append(child)
  
  def find(self, prefix):
    """
    Returns the node that matches the given prefix, or None if not found.
    We will only call this method on the root node, e.g.
    >>> root = Node('')
    >>> node = root.find('te')
    """
    # Check if prefix is empty
    if not prefix:
      # If so, that means that this node matches given prefix
      return self
    
    # Loop through children to identify which one has correct prefix
    for child in self.get_children():
      # Check if last letter of child's prefix matches first letter of prefix
      if child.get_prefix()[-1] == prefix[0]:
        # Recurse to find correct node
        return child.find(prefix[1:])
  
  def words(self):
    """
    Returns a list of complete words that start with my prefix.
    The list should be in lexicographical order.
    """
    # Initialise a list to store words
    words = []
    # Check if current node is a word
    if self.is_word() is True:
      # Add to list if it is
      words.append(self.get_prefix())
    
    # Loop through children to find any other words
    for child in self.get_children():
      # Recurse and add to list
      words += child.words()
    
    # Need a sorted list as return value
    return sorted(words)


if __name__ == '__main__':
  # Write your test code here. This code will not be run by the marker.

  # The first example in the question.
  root = Node('')
  for word in ['tea', 'ted', 'ten']:
    root.add_word(word)
  node = root.find('te')
  print(node.get_prefix())
  print(node.is_word())
  print(node.words())

  # The second example in the question.
  root = Node('')
  for word in ['inn', 'in', 'into', 'idle']:
    root.add_word(word)
  node = root.find('in')
  print(node.get_prefix())
  children = node.get_children()
  print(sorted([n.get_prefix() for n in children]))
  print(node.is_word())
  print(node.words())

  # The third example in the question.
  with open('the-man-from-snowy-river.txt') as f:
    words = f.read().split()
  root = Node('')
  for word in words:
    root.add_word(word)
  print(root.find('th').words())