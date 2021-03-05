# Notable Nicknames (Week 1 Part 2: Functions)

## Instructions
Let's make a program that detects if a user's input is a *notable nickname*!

A *notable nickname* is a name that is **at least 5 characters long** and **starts with the letter N**.

Here's an example of how your program should work:
```
Type a nickname: Noddy
That nickname is notable!
```

Names that are **shorter than 5 characters long** or **don't start with N** are not so notable:
```
Type a nickname: Bazza
That nickname is not so notable!
```

Your program should ask the user for input and then use a *function* to help you decide if it is notable. We've started by defining a function for you, called `is_notable`.

**Finish the function, ask the user for a nickname, call the function to decide if the nickname is notable, then print the result!**

Here are some examples of how your function should work:

**When called like this ...** | **... the function should return:**
---|---
`is_notable('Noddy')` | 'notable'
`is_notable('Bazza')` | 'not so notable'
`is_notable('Nim')` | 'not so notable'

## Directory Files
- [Program](program.py)
- [Pseudocode](pseudocode.txt)