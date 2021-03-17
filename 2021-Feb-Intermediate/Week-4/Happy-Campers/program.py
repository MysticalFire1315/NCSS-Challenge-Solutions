def main():
    groups = {'Perth Pilot Academy': 5, 'Melbourne Mime Society': 4, 'Canadian Cat Club': 12, 'Guide Dogs Guild': 22, 'Coriander Protection League': 3, "Teddy's Tap Dance Troupe": 14, 'Sydney Soup Society': 5, 'Kiwi Kayak Collective': 32, 'Inner-City Ibis Initiative': 1, 'Untitled Union': 9, 'Smashed Avo Advocates': 16}

    beds = int(input("How many beds at the camp? "))
    print("The groups that fit are:")
    for group in groups:
        if beds >= groups[group]:
            print(group)
    return

if __name__ == "__main__":
  main()