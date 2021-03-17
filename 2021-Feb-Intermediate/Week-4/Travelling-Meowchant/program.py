def main():
    item_dict = {}
    item = input("Item: ")
    while item:
        freq = int(input("Number sold: "))
        if item not in item_dict.keys():
            item_dict[item] = freq
        else:
            item_dict[item] += freq
        item = input("Item: ")
    
    print("Total sales for today:")
    for item in item_dict.keys():
        print(f"{item} : {item_dict[item]}")
    return

if __name__ == "__main__":
    main()