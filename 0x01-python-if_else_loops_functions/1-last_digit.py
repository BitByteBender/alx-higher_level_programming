#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

txt_less = "Last digit of {} is {} and is less than 6 and not 0"
txt_greater = "Last digit of {} is {} and is greater than 5"
last_digit = abs(number) % 10

if (number < 0):
    last_digit = -last_digit

if (last_digit > 5):
    print(txt_greater.format(number, last_digit))
elif (last_digit == 0):
    print("Last digit of {} is {} and is 0".format(number, last_digit))
else:
    print(txt_less.format(number, last_digit))
