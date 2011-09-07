#!/usr/bin/python

#Filename: numgen.py
#Author: Jithu Sunny
#Date: June 21, 2011

import time
from random import randint

def main():
    '''Generates a random 10-digit number'''

    while True:
        first = randint(0, 9)
        rest = randint(100000000,999999999)
        print '%d%d' %(first, rest) 
#'number' is made by combining 'first' and 'rest' parts because of the inability to pass 0000000000 as an argument to randint()

main()
