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
    # Call the function again (recursively), on the rest of the string minus the first letter, + 1 to increment as you go
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
    
    # Save letters in key 
    key = "th"
    
    # Base case
    if len(word) <= 1: 
        return 0 
    
    # Recursive case
    if key in word[0:2]: 
        return 1 + count_th(word[1:])
    else: 
        return count_th(word[1:])
    


