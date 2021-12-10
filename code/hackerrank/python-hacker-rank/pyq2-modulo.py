#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 == 1 or (n % 2 == 0 and n in range(6, 21)):
        print("Weird") 
    else:  
        print("Not Weird")    

        
# Q: what is .strip()?  input strip out text format?  
# A: Removes any leading and trailing white spaces.  In case input has white spaces.  
# If .strip(chars) parameter specified, it will strip leading and trailing matching characters.  

# Q why funciton called "if __name__ = '__main__': ?  Why dunders? 

# Python3 program to demonstrate the use of
# strip() method

string = """ geeks for geeks """

# prints the string without stripping
print(string)

# prints the string by removing leading and trailing whitespaces
print(string.strip())

# prints the string by removing geeks
print(string.strip(' geeks'))

""" 
Output:  
    geeks for geeks     # not stripping leading spaces
geeks for geeks  # stripped leading spaces
for  # stripped space and "geeks"  
"""
