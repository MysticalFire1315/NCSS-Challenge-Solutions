from exceptions import PermissionDenied


class Post:
  def __init__(self, content, author):
    """
    Creates a new thread with a title and an initial first post.
    The author of the first post at the time of thread creation is the owner of the thread.
    The owner cannot change once the thread is created.
    """
    pass
  
  def get_author(self):
    """
    Returns the author of the post.
    """
    pass
  
  def get_content(self):
    """
    Returns the content of the post.
    """
    pass
  
  def get_upvotes(self):
    """
    Returns a single integer representing the total number of upvotes.
    """
    pass
  
  def set_content(self, content, by_user):
    """
    Called when the given user wants to update the content.
    * raises PermissionDenied if the given user is not the author.
    """
    pass
  
  def upvote(self, by_user):
    """
    Called when the given user wants to upvote this post.
    A user can only perform an up vote *once*.
    """
    pass
  

class Thread:
  def __init__(self, title, first_post):
    """
    Creates a new thread with a title and an initial first post.
    The author of the first post is also the owner of the thread.
    The owner cannot change once the thread is created.
    """
    pass

  def get_owner(self):
    """
    Returns the owner of the thread.
    """
    pass
  
  def get_title(self):
    """
    Returns the title of the thread.
    """
    pass
  
  def get_tags(self):
    """
    Returns a sorted list of unique tags.
    """
    pass
  
  def get_posts(self):
    """
    Returns a list of posts in this thread, in the order they were published.
    """
    pass
  
  def publish_post(self, post):
    """
    Adds the given post object into the list of posts.
    """
    pass
  
  def remove_post(self, post, by_user):
    """
    Allows the given user to remove the post from this thread.
    Does nothing if the post is not in this thread.
    * raises PermissionDenied if the given user is not the author of the post.
    """
    pass
  
  def set_title(self, title, by_user):
    """
    Allows the given user to edit the thread title.
    * raises PermissionDenied if the given user is not the owner of the thread.
    """
    pass
  
  def set_tags(self, tag_list, by_user):
    """
    Allows the given user to replace the thread tags (list of strings).
    * raises PermissionDenied if the given user is not the owner of the thread.
    """
    pass


class Forum:
  def __init__(self):
    """
    Perform initialisation of a new forum object, as needed.
    """
    pass
  
  def get_threads(self):
    """
    Returns a list of threads in the forum, in the order that they were published.
    """
    pass
  
  def publish(self, title, content, author):
    """
    Creates a new thread with the given title and adds it to the forum.
    The content and author are provided to allow you to create the first post object.
    Forum threads are stored in the order that they are published.
    Returns the new thread.
    """
    pass
  
  def search_by_tag(self, tag):
    """
    Searches all forum threads for any that contain the given tag.
    Returns a list of matching thread objects in the order they were published.
    """
    pass
  
  def search_by_author(self, author):
    """
    Searches all forum threads for posts by the given author.
    Returns a list of matching post objects in any order you like.
    """
    pass
