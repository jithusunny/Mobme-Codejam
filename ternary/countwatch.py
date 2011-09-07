#!/usr/bin/python

#Filename: countwatch.py
#Author: Jithu Sunny
#Date: June 21, 2011

import time

def main():
    '''Prints the number count of each file - n.txt in every second.'''

    file = [0] * 10 #File pointer array of size 10.

    while 1:
        for i in range (0, 10):
            try:
                file[i] = open(str(i) + '.txt', 'r')

                #f.readlines returns a list whose 'length' or 'number of elements' is the linecount, here the numbercount.
                print 'Number count of', str(i) + '.txt: ', len(file[i].readlines())

                file[i].close()
            except IOError:
                print 'Number count of', str(i) + '.txt: 0'
        print
        time.sleep(1)
main()
