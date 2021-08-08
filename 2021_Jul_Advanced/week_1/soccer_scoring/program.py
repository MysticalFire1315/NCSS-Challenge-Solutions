#! 8 min
#! #1 passed all tests

def soccer_scoring():
  # Read from file
  file_contents = []
  for line in open("commentary.txt", "r"):
    file_contents.append(line.strip())
  
  # Get team names
  line_one = file_contents[0].split()
  teams = {}
  teams = {
    line_one[0] : 0,
    line_one[2] : 0}
  
  # Loop through rest of file lines
  for line in range(1, len(file_contents)):
    # Split line into individual words
    words = file_contents[line].split()
    teams[words[0]] += 1
  
  if teams[line_one[0]] > teams[line_one[2]]:
    print(f"{line_one[0]} {teams[line_one[0]]}")
    print(f"{line_one[2]} {teams[line_one[2]]}")
  else:
    print(f"{line_one[2]} {teams[line_one[2]]}")
    print(f"{line_one[0]} {teams[line_one[0]]}")

if __name__ == "__main__":
  soccer_scoring()