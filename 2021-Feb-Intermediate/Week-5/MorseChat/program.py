def main():
    morsedict = {}
    with open('morsecode.txt', 'r') as f:
        text = f.read().split('\n')
    for index in range(len(text)):
        coded = text[index].split()
        morsedict[coded[0]] = coded[1]
    
    message = input("Message: ")
    translation = ''
    for index in range(len(message)):
        word = message[index]
        try:
            translation += morsedict[word.upper()]
        except KeyError:
            translation += "/"
            translation += " "
    print(translation[:-1])
    return

if __name__ == "__main__":
    main()