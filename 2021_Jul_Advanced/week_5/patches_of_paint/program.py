#! 14 min 18 sec
#! #1 passed all tests

from sklearn.cluster import DBSCAN
from math import sqrt

def patches_of_paint():
  # Read file to get picture
  patches = read_into_array('patches.txt')
  
  # Get coordinates of paint (%)
  paint = get_coordinates(patches, '%')
  
  # First check if there are any paint patches at all
  if paint == []:
    # If not patches, exit
    print('0 patches')
    return
  
  # Use sklearn's DBSCAN to cluster points
  
  # Parameter `eps` is the minimum distance between points for them to count as
  # part of the same cluster. In this case, diagonals are also included, so the
  # distance between two diagonal points can be found using Pythagoras
  #  > c = sqrt(a + b)
  # In this case, a and b are both 1, so c = sqrt(2)
  
  # As these points are paint spots, minimum number of points to form a cluster
  # is 1
  dbscan_obj = DBSCAN(eps=sqrt(2), min_samples=1).fit(paint)
  
  # Get the number of paint patches. DBSCAN object's `labels_` property gives
  # each point a label to indicate which cluster they belong to. Cluster naming
  # starts from 0, so add 1 to the maximum to tell the number of cluster groups
  paint_clusters = max(dbscan_obj.labels_) + 1
  
  # Format grammar
  if paint_clusters == 1:
    print(f'{paint_clusters} patch')
  else:
    print(f'{paint_clusters} patches')

def get_coordinates(array, item):
  """
  Get a list of coordinates where `item` shows up in the array.
  
  :param array: The array to look through.
  :type array: list
  
  :param item: The item to find in the array.
  :type item: str
  
  :return: A list of coordinates (sub-arrays) representing where the item were
           found.
  :rtype: list
  """
  coordinates = []
  for y in range(len(array)):
    for x in range(len(array[y])):
      if array[y][x] == item:
        coordinates.append(tuple([y, x]))
  return coordinates

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

if __name__ == '__main__':
  patches_of_paint()