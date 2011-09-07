#!/usr/bin/python

#Filename: invariant.py
#Author: Jithu Sunny
#Date: June 23, 2011

def filter_list(number_list):
    '''Filters out unwanted numbers like 1111, 2222,... 9999 from list'''

    for i in range(1, 10):
        number_list.remove(int(str(i) * 4))
    number_list.remove(6174)#edge case
      
    return number_list


def print_(dict):
    '''A custom print function to print the dictionary'''

    print 'Iteration 	Total Count of Numbers'
    for key, value in dict.items():
        print '    ', key, '\t\t    ', value
    return


def iteration_counter(number):
    '''Returns the number of iterations for each number'''

    if number == 6174:
        return 0
    else:
        number_as_list = list(str(number))

        while len(number_as_list) != 4:
            number_as_list.append('0')

        number_as_list.sort()
        
        asc_number = int(''.join(number_as_list))

        number_as_list.reverse()

        desc_number = int(''.join(number_as_list))

        return 1 + iteration_counter(desc_number - asc_number)


def main():
    iteration_dict = {}#dictionary to store iteration count

    numbers_list = range(1000, 10000)
    numbers_list = filter_list(numbers_list)#numbers_list contains all required numbers.
    
    for item in numbers_list:
        iterations = iteration_counter(item)

        if iterations in iteration_dict: #enter iteration count into dictionary
            iteration_dict[iterations] += 1
        else:
            iteration_dict[iterations] = 1

    iteration_dict[1] += 1 #iteration count of the edge case 6714

    print
    print_(iteration_dict)#print result
    print

main()
