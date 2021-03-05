# Formula Extreme (Week 1 Part 2: Putting it all together!)

## Instructions
You've decided to start a career as a jetski racer. But your jetski measures its speed in knots. What even are those?

Your program should ask for a speed in knots and convert it to kilometers per hour, then print it out with a short message.

For example:
```
Speed (kn): 60
111.1 km/h - Radical!
```

Or, another example with a slower speed:
```
Speed (kn): 10.3
19.1 km/h - Go faster!
```

Finish the `to_kmh` function we've started for you to convert the speed from knots to kilometers per hour, *rounding to 1 decimal place*. Use this function when you write the rest of your code.

**Use the formula below for your conversion**

$$km/h = 1.852 * knots$$

Your program should print out a message to encourage you depending on the *rounded speed*:
**Speed Range** | **Message**
---|---
<60 km/h | Go faster!
≥60 km/h and <100 km/h | Nice one.
≥100 km/h and <120 km/h | Radical!
≥120 km/h | Whoa! Slow down!

## Directory Files
- [Program](program.py)
- [Pseudocode](pseudocode.txt)