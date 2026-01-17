#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = str(number)[-1]
last_digit = int(last_digit)
if last_digit > 5:
    situation = "and is greater than 5"
elif last_digit < 6 and last_digit != 0:
    situation = "and is less than 6 and not 0"
else:
    situation = "and is 0"
print(f"Last digit of {number} is {last_digit} {situation}")
