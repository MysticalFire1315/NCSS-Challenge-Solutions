def is_notable(name):
    # Write your function here.
    startingLetter = name[0].upper()
    if len(name) > 5 and startingLetter == "N":
        return "That nickname is notable!"
    else:
        return "That nickname is not so notable!"

def main():
    name = input("Type a nickname: ")
    print(is_notable(name))
    return

if __name__ == "__main__":
    main()