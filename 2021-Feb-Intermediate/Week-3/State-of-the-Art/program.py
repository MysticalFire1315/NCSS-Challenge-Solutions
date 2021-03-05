def main():
    proposals = []
    for i in range(3):
        mag_name = input("Magazine name: ")
        while "art" not in mag_name.lower():
            mag_name = input("Magazine name: ")
        proposals.append(mag_name)
    proposals.sort()
    proposals = proposals[::-1]
    print(f"Proposals: {", ".join(proposals)}")
    return

if __name__ == "__main__":
    main()