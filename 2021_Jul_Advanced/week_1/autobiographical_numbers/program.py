#! 13 min 45 sec
#! #1 5 tests passed
#! #2 passed all tests

def autobiographical_numbers():
  # Get number
  number = input("Number: ")
  
  # Autobiographical numbers cannot have >10 digits
  if len(number) > 10:
    print(f"{number} is not autobiographical.")
    return
  
  # Initialise a dict to store num of each digit
  auto_dict = {}
  for num in range(len(number)):
    auto_dict[num] = 0
  
  # Loop through each digit to add to dict
  for digit in range(len(number)):
    try:
      auto_dict[int(number[digit])] += 1
    except:
      print(f"{number} is not autobiographical.")
      return
  
  processed = ""
  # Loop through to ensure autobiographical
  for val in auto_dict.values():
    processed += str(val)
  
  if processed == number:
    print(f"{number} is autobiographical.")
  else:
    print(f"{number} is not autobiographical.")
  

if __name__ == "__main__":
  autobiographical_numbers()