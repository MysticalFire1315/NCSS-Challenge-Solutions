def main():
    print("Let's go!")
    arrival = input("Are we there yet? ")
    while "yes" not in arrival.lower():
        print("Aww...")
        arrival = input("Are we there yet? ")
    print("Hooray!!!")
    return

if __name__ == "__main__":
    main()