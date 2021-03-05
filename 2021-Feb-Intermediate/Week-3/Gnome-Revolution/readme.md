# Gnome Revolution (Week 3 Part 2: Putting it all together)

## Instructions
Loben the gnome has just finished sprucing up his house, but his garden is looking bare. He's invited all his gnome friends over for a flower planting day.

Write a program to help Loben track which kinds of flowers are planted and how many are planted in total.

Your program should keep asking for a species of flower until none are entered. When a species is entered, ask for how many were planted, then update the total number of flowers. If it's the *first of this species to be planted*, record the species. As flowers are entered, print messages to notify everyone of progress.

Here's an example of how your program should work:
```
Let's get planting everyone!
What kind of flower did you plant? daffodil
How many did you plant? 7
Our first daffodils! We just planted 7 of them!
What kind of flower did you plant? allium
How many did you plant? 12
Our first alliums! We just planted 12 of them!
What kind of flower did you plant? daffodil
How many did you plant? 11
Fantastic! We just planted 11 more daffodils!
What kind of flower did you plant? 
Nice work, everyone! We planted 30 flowers!
These are all the kinds of flowers we planted today:
🏵️ allium
🏵️ daffodil
```

When the day is done, print out the total number of flowers planted. Then print out all the species in **alphabetical** order.

Here's a longer example:
```
Let's get planting everyone!
What kind of flower did you plant? wax begonia
How many did you plant? 36
Our first wax begonias! We just planted 36 of them!
What kind of flower did you plant? tulip
How many did you plant? 20
Our first tulips! We just planted 20 of them!
What kind of flower did you plant? wax begonia
How many did you plant? 8
Fantastic! We just planted 8 more wax begonias!
What kind of flower did you plant? chrysanthemum
How many did you plant? 29
Our first chrysanthemums! We just planted 29 of them!
What kind of flower did you plant? chrysanthemum
How many did you plant? 6
Fantastic! We just planted 6 more chrysanthemums!
What kind of flower did you plant? 
Nice work, everyone! We planted 99 flowers!
These are all the kinds of flowers we planted today:
🏵️ chrysanthemum
🏵️ tulip
🏵️ wax begonia
```

***Note**: At the end when no species is entered, it doesn't ask for a number. Be careful where you put your second `input`.*