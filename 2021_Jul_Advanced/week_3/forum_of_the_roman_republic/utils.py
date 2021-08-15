def sorted_dict_vals(dict_obj):
  """
  Get a list of values sorted by key from the dictionary provided.

  :param dict_obj: The dictionary to get values from.
  :type dict_obj: dict

  :return: A list of values sorted by key from the dictionary provided.
  :rtype: list
  """
  # First sort by key
  sorted_keys = sorted(dict_obj.keys())
  
  # Initialise a list to return
  return_list = []
  for key in sorted_keys:
    return_list.append(dict_obj[key])
  
  return return_list

def linear_search(list_to_search, search_item):
  """
  Perform linear search on a list (single element).

  :param list_to_search: The list to search in.
  :type list_to_search: list

  :param search_item: The item to search for.
  :type search_item: any

  :return: The index the item was found at.
  :rtype: int

  Note: From SDD Course Specs document
  """

  # Let i = 1
  index = 0
  # Let FoundIt = false
  found = False
  # Get RequiredName
  to_be_found = search_item

  # WHILE FoundIt is false AND i <= number of names
  while found is False and index < len(list_to_search):
    # IF Names(i) <> RequiredName THEN
    if list_to_search[index] != to_be_found:
      # i = i + 1
      index += 1
    # ELSE
    else:
      # Let FoundIt = true
      found = True
  
  if found is True:
    return index
  else:
    raise ValueError