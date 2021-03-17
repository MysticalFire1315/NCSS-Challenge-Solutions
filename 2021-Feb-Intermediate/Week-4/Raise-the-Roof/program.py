def main():
    bread_dict = {}
    for loop in range(5):
        new_bread = False
        while new_bread is False:
            name = input("Name: ")
            bread = input("What kind of bread are you bringing? ")
            if bread not in bread_dict.keys():
                bread_dict[bread] = name
                print(f"{bread_dict[bread]} is bringing a {bread}!")
                new_bread = True
            else:
                print("Someone else is bringing that already.")
    
    print("The party is organised! Here's what's on the menu:")
    for bread in bread_dict.keys():
        print(f"{bread}: {bread_dict[bread]}")
    return

if __name__ == "__main__":
    main()