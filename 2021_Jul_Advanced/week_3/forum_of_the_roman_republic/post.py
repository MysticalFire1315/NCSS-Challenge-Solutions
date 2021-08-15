from exceptions import PermissionDenied


class Post:
  def __init__(self, content, author):
    """
    Creates a new Post by the author with the given content.
    You will need to track up votes more cleverly than previously because
    a user is only allowed to vote *once*.
    """
    # Set author and content
    self._author = author
    self._content = content

    # Set other details (upvotes, downvotes, etc) to default
    self._upvotes = 0
    self._upvoters = []
    self._downvotes = 0
    self._downvoters = []
  
  def get_author(self):
    """
    Returns the author of the Post.
    """
    return self._author
  
  def get_content(self):
    """
    Returns the content of the Post.
    """
    return self._content
  
  def get_upvotes(self):
    """
    Returns a non-negative integer representing the total number of upvotes.
    """
    return self._upvotes
  
  def get_downvotes(self):
    """
    Returns a non-negative integer representing the total number of downvotes.
    """
    return self._downvotes
  
  def set_content(self, content, by_user):
    """
    Called when the given user wants to update the content.
    * raises PermissionDenied if the given user is not the author.
    """
    # Check if user is the author
    if by_user != self._author:
      # Content can only be updated if user is the author
      raise PermissionDenied
    
    # Update content
    self._content = content
  
  def upvote(self, by_user):
    """
    Called when the given user wants to upvote this post.
    A user can only perform an up vote *once*.
    """
    # Check if user is already in list of users that have upvoted the post
    if by_user in self._upvoters:
      # If user has already upvoted, do nothing
      return
    
    # User can either upvote or downvote a post
    if by_user in self._downvoters:
      # Remove user from list of downvoters
      self._downvoters.remove(by_user)
      # Decrement the number of downvotes
      self._downvotes -= 1
    
    # Otherwise, increment upvote count and add user to list of upvoters
    self._upvotes += 1
    self._upvoters.append(by_user)
  
  def downvote(self, by_user):
    """
    Called when the given user wants to downvote this post.
    A user can only perform a down vote *once*.
    """
    # Check if user is already in list of users that have downvoted the post
    if by_user in self._downvoters:
      # If user has already downvoted, do nothing
      return
    
    # User can either upvote or downvote a post
    if by_user in self._upvoters:
      # Remove user from list of upvoters
      self._upvoters.remove(by_user)
      # Decrement the number of upvotes
      self._upvotes -= 1
    
    # Otherwise, increment downvote count and add user to list of downvoters
    self._downvotes += 1
    self._downvoters.append(by_user)