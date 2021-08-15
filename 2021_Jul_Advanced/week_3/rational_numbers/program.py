import random

from rational import Rational, test_rational


ADD = '+'
MINUS = '-'
TIMES = '×'
DIVIDE = '÷'


def random_rational():
  num = random.randint(0, 10)
  den = random.randint(1, 10)
  return Rational(num, den)


test = input('Run tests? ')
if test.lower().startswith('y'):
  test_rational()
else:
  user_answer = '0'
  while user_answer:
    num1 = random_rational()
    num2 = random_rational()
    operator = random.choice((ADD, MINUS, TIMES, DIVIDE))
    print()
    print('What is {} {} {}?'.format(num1, operator, num2))

    if operator == ADD:
      answer = num1 + num2
    elif operator == MINUS:
      answer = num1 - num2
    elif operator == TIMES:
      answer = num1 * num2
    else:
      answer = num1 / num2

    answers = [answer, random_rational(), random_rational(), random_rational()]
    random.shuffle(answers)
    for i, choice in enumerate(answers):
      print('{}) {}'.format(i, choice))
    user_answer = input('> ')
    if user_answer and user_answer.isdigit() and int(user_answer) < 4:
      i = int(user_answer)
      user_answer_rational = answers[i]
      if user_answer_rational == answer:
        print('Correct!')
      else:
        print('Incorrect. The correct answer was: {}'.format(answer))
    else:
      print('Invalid input. The correct answer was: {}'.format(answer))
