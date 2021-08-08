#! 1 min 5 sec
#! #1 passed all tests

def scarce_surname():
  # First get surname
  surname = input("What is your surname? ")
  
  # Check if surname starts with q
  if surname.upper()[0] == "Q":
    print("You have an extremely rare surname!")
  elif "Q" in surname.upper():
    print("You have a rare surname!")
  else:
    print("No Qs here.")

if __name__ == "__main__":
  scarce_surname()