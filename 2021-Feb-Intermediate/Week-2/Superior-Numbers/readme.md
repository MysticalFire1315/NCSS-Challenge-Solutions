# Superior Numbers (Week 2 Part 2: Putting it all together)

## Instructions
Some numbers have personality, while other numbers are just *dull*.

Let's write a program that asks for a list of numbers and **describes** the interesting ones using the personality traits below, while **counting** up all the dull ones without traits.

**Numbers with *none* of these traits are *dull*:**
**Description** | Requirement
---|---
**odd** | It's *not* divisible by 2.
**excessive** | It's *greater than* 10,000
**irksome** | It contains the digit 3.
**arrogant** | It's in the list of `arrogant_numbers`.

Your program should ask for a list of space-separated numbers. For any number with at least one trait, it should print a full description of its personality. Then it should print how many dull numbers were counted.

Here's an example:
```
Enter numbers: 2451 6 29880 1054 9612 4110670
2451 is an odd number.
6 is an arrogant number.
29880 is an excessive arrogant number.
4110670 is an excessive number.
Dull numbers: 2
```

*Note how 2451 and 1054 weren't printed out, because they didn't have personality traits. They were counted as dull numbers intead*

**To break up the task use a function that helps find personality traits for numbers.**

We've started a `find_personality` function for you. But so far it only checks if the number is *odd*. Finish the function by adding checks for the other peronality traits, then use it in your program.

Here are some examples of what your function `find_personality` should output:
**Input** | **Output**
---|---
`find_personality(1599)` | 'odd '
`find_personality(60822)` | 'exessive '
`find_personality(79670)` | 'excessive arrogant '
`find_personality(8305113)` | 'odd excessive irksome '
`find_personality(16)` | ''

*16 is dull, so it returns an empty description. Numbers with traits have spaces at the end.*

Here's one more example of how your program should work:
```
Enter numbers: 29998 203991626 2 7617
29998 is an excessive arrogant number.
203991626 is an excessive irksome number.
7417 is an odd number.
Dull numbers: 1
```

## Directory Files
- [Program](program.py)
- [Pseudocode](pseudocode.txt)