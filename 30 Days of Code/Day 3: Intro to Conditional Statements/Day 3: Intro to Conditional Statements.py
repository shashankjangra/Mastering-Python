#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    while True:
        try:
            N = int(input())
            if N < 1 or N > 100:
                raise ValueError
            break
        except ValueError:
            continue
        
if (N%2) != 0:
    print('Weird')
    
if (N%2) == 0:
    if N>2 and N<5:
        print('Not Weird')
        
    if N>6 and N<21:
        print('Weird')
        
    if N>20:
        print('Not Weird')
