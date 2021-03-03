def main():
    band = input("Band: ")
    songList = input("Songs: ")
    songList = songList.split()

    print(f"Please welcome to the stage, {band}!\nThey will be playing...")
    for index in range(len(songList)):
        print(f"\n🎵 {songList[index]}")
    print(f"\nGive it up for {band}!")
    return

if __name__ == "__main__":
    main()