def main():
    sentence = input("Sentence: ")
    words = sentence.split()

    count = 0
    for index in range(len(words)):
        if words[index].isupper() == True:
            count += 1
    
    print(f"Number of shouted words: {count}")
    return

if __name__ == "__main__":
    main()