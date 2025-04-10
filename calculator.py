# https://github.com/SonyaBW/lab10-SW-AO.git
# Partner 1: Sonya Wong
# Partner 2: Ahmad Osman

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a):
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a   # raise ZeroDivisionError if a == 0

def logarithm(a, b):
    if b <= 0:
        raise ValueError
    return math.log(a,b)# use math library/raise ValueError

def exp(a, b):
    return a**b
