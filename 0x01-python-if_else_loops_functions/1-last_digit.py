#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number >= 0):
 last_digit = str(number)[-1]
else:
 last_digit = str(number)[0] + str(number)[-1]

if (last_digit == "0" or last_digit == "-0"):
 last_digit = "0"

if (last_digit > "5"):
 str = "greater than 5"
elif (last_digit == "0"):
 str = "0"
elif (last_digit < "6" and last_digit != "0"):
 str = "less than 6 and not 0"
print(f"last digit of {number:d} is {last_digit} and is {str}")
