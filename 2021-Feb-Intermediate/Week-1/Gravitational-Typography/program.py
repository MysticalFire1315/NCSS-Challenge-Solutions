def main():
    word = input("Word: ")
    for index in range(len(word)):
        uppercase = word[index].upper()
        print(uppercase)
    print(word.lower())
    return

if __name__ == "__main__":
    main()