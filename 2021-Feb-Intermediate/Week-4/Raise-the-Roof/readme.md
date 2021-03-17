# Raise the Roof (Week 4 Part 2: Adding to a dictionary)

## Instructions
All your friends have gotten into breadmaking recently, so you decide to host a party where they can show off their baking skills.

Write a program to help organise the party. Your program should ask for a person's name and what kind of bread they're bringing, until 5 different breads are being brought. *Each kind of bread cannot be brought more than once.*

Once 5 different breads have been suggested, it should print the list of breads and the people bringing them. Here's an example of how the program should look:

```
Name: Cai
What kind of bread are you bringing? Baguette
Cai is bringing a Baguette!
Name: Rebecca
What kind of bread are you bringing? Bagel
Rebecca is bringing a Bagel!
Name: Heidi
What kind of bread are you bringing? Rye loaf
Heidi is bringing a Rye loaf!
Name: Nevan
What kind of bread are you bringing? Brioche
Nevan is bringing a Brioche!
Name: Cai
What kind of bread are you bringing? Pita
Cai is bringing a Pita!
The party is organised! Here's what's on the menu:
Baguette: Cai
Bagel: Rebecca
Rye loaf: Heidi
Brioche: Nevan
Pita: Cai
```

***Note**: Friends are allowed to bring more than one kind of bread.* In this example, Cai is bringing both a baguette and a pita bread.

Here's another example, where someone suggests a bread that is already being brought. The program prints: ```Someone else is bringing that already.```
```
Name: Cheyenne
What kind of bread are you bringing? Papadum
Cheyenne is bringing a Papadum!
Name: Kirsten
What kind of bread are you bringing? Pumpernickel
Kirsten is bringing a Pumpernickel!
Name: Samir
What kind of bread are you bringing? Pumpernickel
Someone else is bringing that already.
Name: Samir
What kind of bread are you bringing? Papadum
Someone else is bringing that already.
Name: Samir
What kind of bread are you bringing? Cornbread
Samir is bringing a Cornbread!
Name: Shai
What kind of bread are you bringing? Kifli
Shai is bringing a Kifli!
Name: Kayla
What kind of bread are you bringing? Roti
Kayla is bringing a Roti!
The party is organised! Here's what's on the menu:
Papadum: Cheyenne
Pumpernickel: Kirsten
Cornbread: Samir
Kifli: Shai
Roti: Kayla
```

## Directory Files
- [program](program.py)
- [pseudocode](pseudocode.txt)