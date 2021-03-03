def main():
    proposals = []
    for i in range(3):
        mag_name = input("Magazine name: ")
        while "art" not in mag_name.lower():
            mag_name = input("Magazine name: ")
        proposals.append(mag_name)
    proposals.sort()
    display = ""
    for item in proposals:
        display = f", {item} {display}"
    print(f"Proposals: {display[2:]}")
    return

if __name__ == "__main__":
    main()