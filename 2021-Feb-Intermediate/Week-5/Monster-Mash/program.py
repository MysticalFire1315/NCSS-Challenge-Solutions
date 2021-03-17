def main():
    filename = input("Chapter file: ")
    with open(filename, 'r') as f:
        chapter = f.read().split()
    display = ""
    for index in range(len(chapter)):
        if index%5 == 0 and index < 200:
            display += chapter[index] + " "
    print(display)
    return

if __name__ == "__main__":
    main()