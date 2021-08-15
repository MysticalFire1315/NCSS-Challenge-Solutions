from post import Post
from thread import Thread
from time import time
from utils import sorted_dict_vals


class Forum:
  def __init__(self):
    """
    Perform initialisation of a new Forum object, as needed.
    """
    # Set thread list
    self._thread_list = {}
  
  def get_threads(self):
    """
    Returns a list of Threads in the Forum, in the order that they were published.
    """
    return sorted_dict_vals(self._thread_list)
  
  def publish(self, title, content, author):
    """
    Creates a new Thread with the given title and adds it to the Forum.
    The content and author are provided to allow you to create the first Post object.
    Threads are stored in the order that they are published.
    Returns the new Thread object.
    """
    # Initialise the new thread
    thread = Thread(title, Post(content, author))

    # Store thread in list of threads
    self._thread_list[time()] = thread

    # Return new Thread object
    return thread
  
  def search_by_tag(self, tag):
    """
    Searches all forum Threads for any that contain the given tag.
    Returns a list of matching Thread objects in the order they were published.
    """
    # Initialise a dict to store matching Thread objects
    matching_threads = {}

    # Search for matching tags
    for time_posted, thread in self._thread_list.items():
      if tag in thread.get_tags():
        matching_threads[time_posted] = thread
    
    # Return matching Thread objects
    return sorted_dict_vals(matching_threads)
  
  def search_by_author(self, author):
    """
    Searches all forum Threads for Posts by the given author.
    Returns a list of matching Post objects in any order you like.
    """
    # Initialise a dict to store matching Post objects
    matching_posts = []

    # Loop through all threads
    for thread in self._thread_list.values():
      # Loop through all posts
      for post in thread.get_posts():
        # Check if post author matches given author
        if post.get_author() == author:
          matching_posts.append(post)
    
    # Return matching Post objects
    return matching_posts