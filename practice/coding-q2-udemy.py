"""
Write a function to add the number of repeating characters as letter + num, case sensitive.  

Ex: AAABCCC should be A3B1C3  
Ex: DDDaaBBBb should be D3a2B3b1

-----  

My steps:  
Take the first item of array  
See if the next item is the same character (case sensitive).  
While same character, add to running total of number of same characters. 
When it changes to another number, add letter + number to a results list to return.  
With the new character, repeat steps.  
When end of array is reached, return final string.

"""

def compress(input): 
    result = ''  # empty string  

    # initialize char and count variables  
    if len(input) < 1:  
        print(result, "empty")
        return result  

    char = input[0]
    count = 1 
    print(char, count)

    if len(input) < 2: 
        result = char + str(count)
        print(result, "one char")
        return result


    for i in range(1, len(input)): 
        if input[i] == char: 
            count += 1
        else:  
            # A different character encountered. 
            # write to result  
            # reset char and count variables
            result = result + char + str(count)
            print(result, "else loop")
            char = input[i]
            count = 1

    print("result", result)
    return result





# Test cases  
# Ex: AAABCCC should be A3B1C3  
# Ex: DDDaaBBBb should be D3a2B3b1



# Call function with test cases  
print(compress('A'))

result1 = compress('AAABCCC') 
print(result1)

result2 = compress('DDDaaBBBb') 
print(result2)

