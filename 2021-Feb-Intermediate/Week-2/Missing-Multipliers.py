def main():
    table = int(input("Times table: "))
    step = int(input("Step: "))
    for num in range(3, 13, step):
        print(f"{table} x [ ] = {table*num}")
    return

if __name__ == "__main__":
    main()