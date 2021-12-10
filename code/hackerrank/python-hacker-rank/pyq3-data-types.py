i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.

# Read and save an integer, double, and String to your variables.
anum = int(input())
bnum = round(float(input()), 1)
cstr = input()
# Print the sum of both integer variables on a new line.
print(i + anum)

# Print the sum of the double variables on a new line.
print(d + bnum)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + cstr)


# round(number, ndigits), rounds floating point to ndigits, default is 0.  
# input() seems to read one line at a time from input file.  
# input is always in string format.  
# declaring variable before assigning is not needed in Python, but C++ needs it. 
