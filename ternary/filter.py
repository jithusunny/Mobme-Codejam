#!/usr/bin/python

#Filename: filter.py
#Author: Jithu Sunny
#Date: June 21, 2011

def main():
    '''Depending on the 'first' digit, the 'number' is stored into the respective file.'''

    while 1:
        number = raw_input() 
        first_digit = int(number)/1000000000
        
        try:
            f = open(str(first_digit) + '.txt', 'a')
            f.write(number + '\n')
        finally:
            f.close()

main()
