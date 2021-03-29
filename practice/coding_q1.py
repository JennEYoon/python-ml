"""
# Python Interview Prep - Coding Q1
# 3/28, 2021 Sunday 11:00 pm start - 3/29 Monday  
# Jennifer E Yoon  

Q1) Given an array of integers (positibe and negative numbers), 
write a program that can find the largest continuous sum.  
Return the sum amount, don't need to return the sequence.  

ex: 
A = [7, 8, 9]           = 24
B = [-1, 7, 8, 9, -10]  = 24 
C = [2, 3, -10, 9, 2]   = 11 
D = [2, 11, -10, 9, 2]  = 14
E = [12, -10, 7, -8, 4, 6] = 12

Possible answer cases:  
1) Max number, 1 digit  
2) Sum of all digits  
3) Largest valued continuous segment composed of all positive numbers, 
   length is >1 but less than all.
4) Combination of positive and negative number segments, 
   length is >1 but less than all.
5) Other cases?  Empty list should return NaN.  
"""

def calc(lst):  
    if len(lst)==0: 
        return "NaN" 
    else:      
        a = max(lst)
        b = sum(lst)
        c = 0  # test 
        d = 0  # test

    return max(a, b, c, d)

# Test 1st set:  
A0 = [] 
largest = calc(A0)
print(largest)

A1 = [0, 0, -1, -12. -5] 
largest = calc(A1)
print(largest)


# example, test cases 
A = [7, 8, 9] 
largest = calc(A)  # expect 24  
print(largest)

B = [-1, 7, 8, 9, -10]  
largest = calc(B)  # expect 24
print(largest)


C = [2, 3, -10, 9, 2]   
largest = calc(C)  # expect 11  
print(largest)

D = [2, 11, -10, 9, 2]   
largest = calc(D)  # expect 14
print(largest)

E = [12, -10, 7, -8, 4, 6]   
largest = calc(E)  # expect 12
print(largest)