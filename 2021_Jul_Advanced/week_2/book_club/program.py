#! 15 min 42 sec (was slow due to watching a c-drama while working)
#! #1 2 tests passed
#! #2 passed all tests

def book_club():
  # Get inputs
  lines = []
  user_input = input("Book read: ")
  while user_input:
    lines.append(user_input)
    user_input = input("Book read: ")
  
  # Make friend list and book dict
  friend_list = []
  book_dict = {}
  for line in lines:
    details = line.split(":")
    # Add to book dict
    if details[0] not in book_dict.keys():
      book_dict[details[0]] = [details[1]]
    else:
      book_dict[details[0]].append(details[1])
    
    # Add to friend list
    if details[1] not in friend_list:
      friend_list.append(details[1])
  
  # Try to sort friends list
  try:
    friend_list.sort()
  except:
    pass
  
  # Loop through to edit book dict to friends who haven't read
  for key in book_dict.keys():
    not_read = ""
    # Loop through friends list
    for friend in friend_list:
      if friend not in book_dict[key]:
        not_read += friend + ", "
    if not_read == "":
      book_dict[key] = "Everyone has read this!"
    else:
      book_dict[key] = not_read[:-2]
  
  # Sort and print
  for book_name in sorted(book_dict.keys()):
    print(f"{book_name}: {book_dict[book_name]}")

if __name__ == "__main__":
  book_club()