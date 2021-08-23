# This a copy of the Node API we put in program.py, in case you delete it.

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
    pass
  
  def get_prefix(self):
    """
    Returns the string prefix for this node.
    """
    pass

  def get_children(self):
    """
    Returns a list of child Node objects, in any order.
    """
    pass
  
  def is_word(self):
    """
    Returns True if this node prefix is also a complete word.
    """
    pass
  
  def add_word(self, word):
    """
    Adds the complete word into the trie, causing child nodes to be created as needed.
    We will only call this method on the root node, e.g.
    >>> root = Node('')
    >>> root.add_word('cheese')
    """
    pass
  
  def find(self, prefix):
    """
    Returns the node that matches the given prefix, or None if not found.
    We will only call this method on the root node, e.g.
    >>> root = Node('')
    >>> node = root.find('te')
    """
    pass
  
  def words(self):
    """
    Returns a list of complete words that start with my prefix.
    The list should be in lexicographical order.
    """
    pass