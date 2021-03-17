import math

def buy_slinkies(tickets):
    # Finish the function to convert tickets to slinkies
    slinky_cost = 3
    return math.floor(tickets/slinky_cost)

# Write the rest of your program here
def main():
    print("Who's here at the carnival today?")
    game_book = {}

    name = input("Name: ")
    while name:
        start_tickets = int(input("Starting tickets: "))
        game_book[name] = start_tickets
        print(f"{name}'s here, starting with {buy_slinkies(start_tickets)} slinkies worth of tickets!")
        name = input("Name: ")

    print("Let the games begin!")
    played = input("Who played? ")
    while played:
        ticket_change = int(input("Tickets won/lost: "))
        if played not in game_book.keys():
            game_book[played] = ticket_change
        else:
            game_book[played] = game_book[played] + ticket_change
            played = input("Who played? ")

    print("End of the day! Let's see how everyone did!")
    for person in game_book.keys():
        print(f"{person} can buy {buy_slinkies(game_book[person])} slinkies.")
    return

if __name__ == "__main__":
    main()