def main():
    dictionary = {'abecedarian': 'Someone learning the alphabet.', 'batrachophagous': 'To feed on frogs.', 'chirotonsor': 'A barber.', 'deltiologist': 'A postcard collector.', 'erinaceous': 'Of hedgehogs.', 'favillous': 'Looking like ashes.', 'grimalkin': 'A cat.', 'nelipot': 'Someone who goes barefoot often.', 'pogonotomy': 'Cutting a beard.', 'psithurism': 'The sound of wind in the trees.', 'scolecophagous': 'To eat worms.', 'xerophagy': 'Eating only dry food.'}

    word = input("Enter a word: ")
    if word.lower() in dictionary.keys():
        print(dictionary[word.lower()])
    else:
        print("Not in the dictionary!")
    return

if __name__ == "__main__":
  main()