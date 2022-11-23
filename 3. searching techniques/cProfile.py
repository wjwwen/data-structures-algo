# -*- coding: utf-8 -*-
"""
cProfile
"""

import time, cProfile

def slow_add(a, b):
    time.sleep(0.5)
    return a+b

def fast_add(a, b):
    return a+b

prof = cProfile.Profile()

def main_func():
    arr = []
    prof.enable()
    for i in range(10):

        if i%2==0:
            arr.append(slow_add(i,i))
        else:
            arr.append(fast_add(i,i))
    prof.disable()
    return arr

main_func()

print(prof.print_stats())