def main():
    tour_locations = ['Netherlands', 'France', 'Switzerland', 'Italy', 'Spain', 'Denmark', 'Sweden', 'Finland']

    # Add your code after this.
    country = input("Country: ")
    if country in tour_locations:
        print(f"{country} is on the list!")
    else:
        print(f"We will not be in {country} this time.")
    return

if __name__ == "__main__":
    main()