def reverse_dict_key_value_pairs(dict_obj):
  """
  Makes all values in a dictionary the keys, while the keys become the values.
  
  :param dict_obj: The dictionary object to manipulate.
  :type dict_obj: dict
  
  :return: The dictionary with all values as keys and keys as values.
  :rtype: dict
  """
  new_dict = {}
  for key, value in dict_obj.items():
    if value in new_dict.keys():
      new_dict[value].append(key)
    else:
      new_dict[value] = [key]
  return new_dict

def read_into_string(filename):
  """
  Read contents of filename into a string.
  
  :param filename: The name of the file to read contents from.
  :type filename: str
  
  :return: The contents of the file as a string.
  :rtype: str
  """
  return ' '.join(read_into_array(filename))

def read_into_array(filename):
  """
  Read contents of filename into an array, where each line takes an element.
  
  :param filename: The name of the file to read contents from.
  :type filename: str
  
  :return: The contents of the file as an array (per line).
  :rtype: list
  """
  return_arr = []
  for line in open(filename, 'r'):
    return_arr.append(line.strip())
  return return_arr