#! 54 min 59 sec
#! #1 3 tests passed (line 19 of forum.py had self._post_list instead of self._thread_list)
#! #2 12 tests passed (set_tags method allowed duplicates)
#! #3 passed all tests

from exceptions import PermissionDenied
from forum import Forum
from thread import Thread
from post import Post

# This file does not need to contain any code. The marker runs program.py and tests the
# classes imported above. You can put any testing code (that won't be run by the marker)
# in the block below.


if __name__ == '__main__':
  # Test your code here. This will not be checked by the marker.
  # Here is the example from the question.
  forum = Forum()
  thread = forum.publish('Battle of Zela', 'Veni, vidi, vici!', 'Caesar')
  thread.set_tags(['battle', 'brag'], 'Caesar')
  thread.publish_post(Post('That was quick!', 'Amantius'))
  thread.publish_post(Post('Hardly broke a sweat.', 'Caesar'))
  thread.publish_post(Post('Any good loot?', 'Amantius'))

  # Search by author
  print("The contents of Caesar's posts:")
  caesar_posts = forum.search_by_author('Caesar')
  print(sorted([p.get_content() for p in caesar_posts]))
  print()

  # Edit content of an existing post
  existing = thread.get_posts()[0]
  existing.set_content('I came, I saw, I conquered!', 'Caesar')

  # Upvote a post:
  existing.upvote('Cleopatra')
  existing.upvote('Brutus')
  existing.upvote('Amantius')
  existing.upvote('Cleopatra')

  print("[{}](+{}) -- {}\n".format(
    existing.get_author(),
    existing.get_upvotes(),
    existing.get_content()
  ))

  # And some access control:
  try:
    thread.set_title('Hijacked!', 'Cleopatra')
  except PermissionDenied:
    print('Cleopatra was not allowed to hijack the thread.')
  
  # Test 13
  print('\n\n Test 13')
  forum = Forum()
  thread = forum.publish('Battle of Zela', 'Veni, vidi, vici!', 'Caesar')
  try:
    thread.set_tags(['battle'], 'Cleopatra')
  except PermissionDenied:
    print('PermissionDenied correctly raised.')
  except:
    print('An exception that was not PermissionDenied was incorrectly raised!')
  else:
    print('Cleopatra should not be allowed to change the tags.')
  print(thread.get_tags())
  try:
    thread.set_tags(['battle'], 'Caesar')
  except PermissionDenied:
    print('PermissionDenied incorrectly raised.')
  except:
    print('An exception that was not PermissionDenied was incorrectly raised!')
  else:
    print('Caesar correctly allowed to change the tags.')
  print(thread.get_tags())
  thread.set_tags(['battle', 'brag'], 'Caesar')
  print(thread.get_tags())
  thread.set_tags(['battle', 'battle', 'battle'], 'Caesar')
  print(thread.get_tags())
  thread.set_tags(['drama', 'battle', 'action', 'latin'], 'Caesar')
  print(thread.get_tags())
  thread.set_tags([], 'Caesar')
  print(thread.get_tags())