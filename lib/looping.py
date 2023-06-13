#!/usr/bin/env python3

def happy_new_year():
    countdown = 10
    while countdown > 0:
      print(countdown)
      countdown = countdown - 1
    print("Happy New Year!")


def square_integers(int_list):
    return [x**2 for x in int_list]

def fizzbuzz():
    for i in range(1,101):
      if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
      elif i % 5 == 0:
        print("Buzz")
      elif i % 3 == 0:
        print("Fizz")
      else:
        print(i)