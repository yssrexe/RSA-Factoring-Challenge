#!/usr/bin/python3
import math

def mission(N):
    last_num = N % 10
    for i in range(2, 10):
        if last_num % i == 0:
            return i

def check_sqrt(value):
    if value.is_integer():
        return 1
    else:
        return 0
