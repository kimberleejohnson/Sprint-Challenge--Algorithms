'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
## Pseudocode 
# Receives a string 
# Base case: Exit out if the string length is less than or equal to 1, since we need two letters for this one to work 
# Evaluates first two letters of string 
# If the first two letters include "th": 
    # Increment the count variable that was initialized at 0 
    # Call the function again (recursively), on the rest of the string minus the first letter
# Else 
    # Call the function again (recursively), on the rest of the string minus the first letter
# Return count 

## Visualization 
# string 
# tring 
# ring
# ing
# ng
# n
# exit out 

def count_th(word):
    
    # TBC
    
    pass