def Peculiar_Puzzle():
  with open("puzzle.txt", "r") as f:
    text = f.read().split("\n")
  codeword = input("Enter a code word: ")
  message = ""
  for line in text:
    if codeword.lower() in line.lower():
      message += line[-1]
  print(f"Hidden message: {message}")

if __name__ == "__main__":
  Peculiar_Puzzle()
