#! 22 min 33 sec
#! #1 0 tests passed (forgot to Ctrl C+V here!)
#! #2 2 tests passed (1 displayed as ¹/₁ instead of 1)
#! #3 10 tests passed (0 displayed as ⁰/₁ instead of 0)
#! #4 passed all tests

SUPER_NUMS = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
SUB_NUMS = ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉']


def gcd(a, b):
  """
  Returns the Greatest Common Divisor between `a` and `b`.
  """
  while b:
    a, b = b, a % b
  return a


class Rational:
  """
  Represents any rational number in fraction form.
  """

  # Implement numerator and denominator variables
  @property
  def numerator(self):
    return self._numerator
  
  @numerator.setter
  def numerator(self, value):
    self._numerator = int(value)
  
  @property
  def denominator(self):
    return self._denominator
  
  @denominator.setter
  def denominator(self, value):
    # Check that denominator value is not 0
    if value != 0:
      self._denominator = int(value)
    else:
      # Otherwise set denominator to 1
      self._denominator = 1
  
  def __cross_multiply(self, other):
    """
    Cross multiplication method. Multiplies the numerator of one rational
    number by the denominator of another, and the denominators together.
    """
    # Multiply A by B's bottom and B by A's bottom
    a_top = self.numerator * other.denominator
    b_top = other.numerator * self.denominator
    bottom = self.denominator * other.denominator
    return a_top, b_top, bottom
  
  def __init__(self, numerator, denominator=1):
    """
    Initialises a rational number with the given numerator and denominator.
    """
    # TODO implement this method.
    # Set numerator and denominator
    self.numerator = numerator
    self.denominator = denominator
    
  def __eq__(self, other):
    """
    Returns True if the two given Rational numbers are equal.
    """
    # TODO implement this method.
    # Use cross-multiplication method to get numerators and denominator
    a_top, b_top, bottom = self.__cross_multiply(other)

    # If numerators match, then they are equal
    if a_top == b_top:
      return True
    else:
      return False

  def __str__(self):
    """
    Returns a string representing this Rational number.
    """
    # TODO implement this method.
    # First convert to inproper fraction
    # Do this by subtracting the numerator from the denominator until the
    # numerator's value is less than the denominator's value
    
    # Create instances of numerators and denominators to work with
    top = self.numerator
    bottom = self.denominator
    negative = False
    front = 0

    # Check if numerator is negative
    if top < 0:
      # Convert to positive
      top = top *-1

      # Invert negative flag
      if negative is True:
        negative = False
      elif negative is False:
        negative = True
    
    # Check if denominator is negative
    if bottom < 0:
      # Convert to positive
      bottom = bottom *-1

      # Invert negative flag
      if negative is True:
        negative = False
      elif negative is False:
        negative = True

    while top > bottom:
      top -= bottom
      front += 1
    
    # Simplify numerator and denominator values by dividing by gcd
    greatest_common_divisor = gcd(top, bottom)
    top = str(int(top/greatest_common_divisor))
    bottom = str(int(bottom/greatest_common_divisor))

    # Check if numerator and denominator values are 1
    if top == '1' and bottom == '1':
      front += 1
      # Print => No longer need the fraction display
      return f"""{'-' if negative is True else ''}{front}"""
    
    # Check if numerator is 0
    if top == '0':
      return "0"

    # Handle top and bottom (multiple digits)
    top_display, bottom_display = '', ''
    for digit in range(len(top)):
      top_display += SUPER_NUMS[int(top[digit])]
    for digit in range(len(bottom)):
      bottom_display += SUB_NUMS[int(bottom[digit])]

    

    return f"""{'-' if negative is True
                else ''}{front if front != 0
                else ''}{top_display}/{bottom_display}"""
  
  def __add__(self, other):
    """
    Returns the addition (+) of two Rational numbers.
    """
    # TODO implement this method.
    # Use cross-multiplication method to get numerators and denominator
    a_top, b_top, bottom = self.__cross_multiply(other)

    # Add numerators together
    top = a_top + b_top

    return Rational(top, bottom)
  
  def __mul__(self, other):
    """
    Returns the multiplication (*) of two Rational numbers.
    """
    # TODO implement this method.
    # Multiply numerators together
    top = self.numerator * other.numerator
    # Multiply denominators together
    bottom = self.denominator * other.denominator

    return Rational(top, bottom)

  def __sub__(self, other):
    """
    Returns self minus (-) other of two Rational numbers.
    """
    # TODO implement this method.
    # Use cross-multiplication method to get numerators and denominator
    a_top, b_top, bottom = self.__cross_multiply(other)

    # Add numerators together
    top = a_top - b_top

    return Rational(top, bottom)
  
  def __truediv__(self, other):
    """
    Returns self divided by (/) other.
    """
    # TODO implement this method.
    # Multiply numerator by denominator of each other
    top = self.numerator * other.denominator
    bottom = self.denominator * other.numerator

    return Rational(top, bottom)


def test_rational():
  """
  Put your own tests here.
  This function will never be called during marking.
  """
  # Check that display is as expected
  print(f'Expected: ¹/₂    Actual: {Rational(1, 2)}')
  print(f'Expected: -¹/₂    Actual: {Rational(-1, 2)}')
  print(f'Expected: -¹/₂    Actual: {Rational(1, -2)}')
  print(f'Expected: ¹/₂    Actual: {Rational(-1, -2)}')
  print(f'Expected: 1¹/₂    Actual: {Rational(3, 2)}')
  print(f'Expected: 4    Actual: {Rational(16, 4)}')
  print(f'Expected: 0    Actual: {Rational(0, 1)}')
  

  # Check that equal operator works regardless of fraction simplicity
  print(Rational(-1, 2) == Rational(2, -4))
  print(Rational(1, 2) == Rational(2, 4))

  # Check that addition operator works
  print(Rational(5, 6) == Rational(1, 2) + Rational(1, 3))

  # Check that subtraction operator works
  print(Rational(1, 6) == Rational(1, 2) - Rational(1, 3))

  # Check that multiplication operator works
  print(Rational(0, 1) == Rational(0, 2) * Rational(8, 9))

  # Check that division operator works
  print(Rational(1, 2) == Rational(1, 6) / Rational(1, 3))