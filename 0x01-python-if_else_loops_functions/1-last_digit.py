#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit  = abs(number) % 10
if digit > 5:
  print(f"Last digit of {number} is {digit} and is greater than 5", end="")
elif digit == 0:
  print(f"Last digit of {number} is {digit} and is 0", end="")
else:
  print(f"Last digit of {number} is {digit} and is less than 6 and not 0", end="")
