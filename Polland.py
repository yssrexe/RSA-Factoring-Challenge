#!/usr/bin/python3

def factorize(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return i, number // i
    return None, None
