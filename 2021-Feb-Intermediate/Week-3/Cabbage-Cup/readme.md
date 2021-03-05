# Cabbage Cup (Week 3 Part 2: Indexing a list)

## Instructions
You're refereeing a snail race. Sometimes snails curl up and go to sleep during races, which disqualifies them.

We've given you a list called `racers`, which contains the names of the snails in the race. 

Write a program to help you keep track of the race. It should ask for the name of a racer who's gone to sleep and replace their name in the list with `'Disqualified'`. If that name isn't in the list, it should leave the list unmodified and print a message saying all the racers are still awake.

Here's an example of how your program should look:
```
And the line up is: Dash, Speedy, Lightning, Flash, Sonic
Who's gone to sleep? Speedy
Speedy's has been disqualified!
Remaining racers: Dash, Disqualified, Lightning, Flash, Sonic
```

Here's an example where an inputted name isn't on the list:
```
And the line up is: Dash, Speedy, Lightning, Flash, Sonic
Who's gone to sleep? Gogo
All racers still awake.
Remaining racers: Dash, Speedy, Lightning, Flash, Sonic
```

## Directory Files
- [Program](program.py)
- [Pseudocode](pseudocode.txt)