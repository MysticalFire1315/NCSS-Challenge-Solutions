#! 5 min 9 sec
#! #1 2 tests passed
#! #2 passed all tests

def imei_validator():
  # Get number
  number = input("Enter number: ")
  
  # Split into array of digits
  num_arr = []
  for digit in number:
    num_arr.append(int(digit))
  
  # Move from right to left and double each digit
  for index in range(len(num_arr)-2, 0, -2):
    # Double digit
    doubled = num_arr[index]*2
    
    # Check if doubled digit is >9
    if doubled > 9:
      # Convert to string and get individual digits
      doubled = str(doubled)
      num_arr[index] = int(doubled[0]) + int(doubled[1])
    else:
      # Add doubled straight into num_arr
      num_arr[index] = doubled
  
  # Sum all digits
  total = sum(num_arr)
  
  # Check if summed is divisible by 10
  if total % 10 == 0:
    print("Valid.")
  else:
    print("Invalid.")
  
if __name__ == "__main__":
  imei_validator()