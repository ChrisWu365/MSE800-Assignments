import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    return a ** b

def root(a, b):
    if b == 0:
        raise ValueError("Cannot take the root with an exponent of zero")
    return a ** (1 / b)

def sine(degree):
    return math.sin(math.radians(degree))

def cosine(degree):
    return math.cos(math.radians(degree))

def tangent(degree):
    if degree % 180 == 90:
        raise ValueError("Tangent of angles 90 + n*180 is undefined")
    return math.tan(math.radians(degree))