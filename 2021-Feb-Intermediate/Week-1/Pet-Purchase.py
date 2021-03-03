def main():
    animal = input("What animal would you like? ")
    freq = int(input("How many? "))

    if animal == animal.upper():
        print("Woah! No need to shout, you'll scare the animals!")
    elif freq < 1:
        print("That's sad. No pet for you today.")
    elif freq == 1:
        print(f"Great, here's your {animal.lower()}!")
    else:
        print(f"Ok! {freq} {animal.lower()}s coming right up!")
    return
    
if __name__ == "__main__":
    main()