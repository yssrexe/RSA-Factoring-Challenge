#!/usr/bin/python3
def mission(N):
    last_num = N % 10
    for i in range(3, 10):
        if last_num % i == 0:
            return i

def check_sqrt(value):
    return isinstance(value, (int, float))
