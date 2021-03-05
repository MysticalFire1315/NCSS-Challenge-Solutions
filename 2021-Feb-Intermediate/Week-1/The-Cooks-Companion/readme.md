# The Cook's Companion (Week 1 Part 2: Data types)

## Instructions
Many recipes ask for ingredients in cups (by volume). But it's much more accurate to measure quantities by weight!

One cup of sugar does not weigh the same as one cup of milk because these foods have different densities.

**Write a program to convert a quantity of food from *cups* to *grams*.** Ask the user for:
- the name of the food,
- the quantity in cups, and
- the number of grams per cup (the density).

**Your program should then calculate the quantity in grams as a *float*. You should also round the quantity to *one decimal place*.**

$$grams = cups * density$$

We've started a helper function for you, called `cups_to_grams`, that you should use to do the calculation above. Call this helper function when you write the rest of your program.

Your program should work like this:
```
What food? sugar
How much in cups? 0.255
How many grams per cup? 210
0.255 cups of sugar is 53.6 grams.
```

Here's another example, using a liquid:
```
What food? milk
How much in cups? 1.333
How many grams per cup? 255
1.333 cups of milk is 339.9 grams.
```

## Directory Files
- [Program](program.py)
- [Pseudocode](pseudocode.txt)