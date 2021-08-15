from exceptions import PermissionDenied
from time import time
from utils import linear_search, sorted_dict_vals


class Thread:
  def __init__(self, title, first_post):
    """
    Creates a new thread with a title and an initial first post.
    The author of the first post at the time of thread creation is the owner of the thread.
    The owner cannot change once the thread is created.
    """
    # Set title, owner and list of post
    self._title = title
    self._owner = first_post.get_author()
    self._post_list = {time(): first_post}

    # Set other details (tags, etc)
    self._tag_list = []

  def get_owner(self):
    """
    Returns the owner of the thread.
    """
    return self._owner
  
  def get_title(self):
    """
    Returns the title of the thread.
    """
    return self._title
  
  def get_tags(self):
    """
    Returns a sorted list of unique tags.
    """
    return sorted(self._tag_list)

  def get_posts(self):
    """
    Returns a list of Post objects in this thread, in the order they were published.
    """
    return sorted_dict_vals(self._post_list)
  
  def publish_post(self, post):
    """
    Adds the given Post object into the list of Posts in this thread.
    """
    self._post_list[time()] = post
  
  def remove_post(self, post, by_user):
    """
    Allows the given user to remove the Post from this thread.
    Does nothing if the Post is not in this thread.
    * raises PermissionDenied if the given user is not the author of the post.
    """
    # Check if post in list of posts
    if post not in self._post_list.values():
      # Do nothing
      return
    
    # Check if user removing the post is the author of the post
    if by_user != post.get_author():
      raise PermissionDenied
    
    # Identify the time the post was published
    index_found = linear_search(list(self._post_list.values()), post)
    time_posted = list(self._post_list.keys())[index_found]

    # Remove post
    self._post_list.pop(time_posted)
  
  def set_title(self, title, by_user):
    """
    Allows the given user to edit the thread title.
    * raises PermissionDenied if the given user is not the owner of the thread.
    """
    # Check if user is thread owner
    if by_user != self._owner:
      raise PermissionDenied
    
    # Edit thread title
    self._title = title
  
  def set_tags(self, tag_list, by_user):
    """
    Allows the given user to replace the thread tags (list of strings).
    * raises PermissionDenied if the given user is not the owner of the thread.
    """
    # Check if user is thread owner
    if by_user != self._owner:
      raise PermissionDenied
    
    # First empty tag list
    self._tag_list = []
    # Loop through each input tag to ensure that no duplicates occur
    for tag in tag_list:
      if tag not in self._tag_list:
        self._tag_list.append(tag)
    
    # Tags must also be sorted
    self._tag_list.sort()