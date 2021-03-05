def concatenate(array, joiner):
    return_item = ""
    for item in array:
        return_item += item + joiner
    return return_item[:-(len(joiner))]

def main():
    racers = ['Dash', 'Speedy', 'Lightning', 'Flash', 'Sonic']
    joiner = ", "
    print(f"And the line up is: {concatenate(racers, joiner)}")
    
    sleep = input("Who's gone to sleep? ")
    lowercase = [x.lower() for x in racers]
    if sleep.lower() in lowercase:
        for index in range(len(racers)):
            if sleep.lower() == racers[index].lower():
                print(f"{sleep} has been disqualified!")
                racers[index] = "Disqualified"
    else:
        print("All snails still awake.")
    
    print(f"Remaining racers: {concatenate(racers, joiner)}")
    return

if __name__ == "__main__":
    main()