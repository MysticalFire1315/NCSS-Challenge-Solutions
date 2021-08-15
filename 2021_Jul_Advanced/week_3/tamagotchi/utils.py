def print_sorted_dict(dict_obj):
  """
  Printed the contents of a dictionary object alphabetically by key.

  :param dict_obj: A dictionary object to print the contents of.
  :type dict_obj: dict
  """
  # Get the keys of the dictionary object and sort alphabetically
  for key in sorted(dict_obj.keys()):
      print(dict_obj[key])