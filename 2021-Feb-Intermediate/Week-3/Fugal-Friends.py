import math

def main():
    start = float(input("Start (g): "))
    end = float(input("Finish (g): "))

    hours = 0
    while end > start:
        start = start + 0.6*start
        hours += 1
    
    print(f"The loaf would need to rise for {hours} hours.")
    return

if __name__ == "__main__":
    main()