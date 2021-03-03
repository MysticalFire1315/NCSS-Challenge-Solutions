def main():
    print("Let's get planting everyone!")
    flower_dict = {}

    flower = input("What kind of flower did you plant? ")
    while flower:
        freq = int(input("How many did you plant? "))
        if flower not in flower_dict.keys():
            flower_dict[flower] = freq
            print(f"Our first {flower}s! We just planted {freq} of them!")
        else:
            flower_dict[flower] += freq
            print(f"Fantastic! We just planted {freq} more {flower}s!")
        flower = input("What kind of flower did you plant? ")
    
    total = sum(flower_dict.values())
    print(f"Nice work, everyone! We planted {total} flowers!")

    print("These are all the kinds of flowers we planted today: ")
    if flower_dict:
        flower_types = list(flower_dict.keys())
        flower_types.sort()
        for item in flower_types:
            print(f"🏵️ {item}")
    return

if __name__ == "__main__":
    main()