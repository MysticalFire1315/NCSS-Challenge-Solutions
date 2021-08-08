def Nom_nom_nomination():
  filename = input("Enter a city file: ")
  with open(filename, 'r') as f:
    nominees = f.read().split('\n')
  filtered = []
  for item in nominees:
    if item not in filtered and item != "":
      filtered.append(item)
  print("And the nominees are...")
  if filtered != []:
    for item in sorted(filtered):
      print(f"🥑 {item}")

if __name__ == "__main__":
  Nom_nom_nomination()
