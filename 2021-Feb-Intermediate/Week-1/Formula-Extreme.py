def to_kmh(knots):
    # Calculate the speed in km/h
    return round(1.852*knots, 1)

# Write the rest of your program here
def main():
    speed = float(input("Speed (kn): "))
    speed = to_kmh(speed)

    if speed < 60:
        print(F"{speed} km/h - Go faster!")
    elif speed < 100:
        print(f"{speed} km/h - Nice one.")
    elif speed < 120:
        print(f"{speed} km/h - Radical!")
    else:
        print(f"{speed} km/h - Whoa! Slow down!")
    return

if __name__ == "__main__":
    main()