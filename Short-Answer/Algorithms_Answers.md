#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear time, O(n): The time this code will take to run depends exclusively on the size of n. Time will increase as N increases, descrease as N decreases. And, only one operation is performed in the single loop. 


b) Polynomial time, O(n^3): A loop within a loop in this code makes the program very inefficient. There are also three iterations happening with each evaluation: establishing j in the first for loop; and, in the second loop, multipling j by 2 and also incrementing the sum. 


c) Linear time, O(n): The code will run exactly n amount of times. We see this in the return statement where the return depends on bunnies - 1. Therefore, runtime depends exclusively on the time of n. 

## Exercise II

### Questions 
- When we say plenty of eggs, does that mean an infinite number of eggs? 

### Assumptions 
- By minimizing the number of dropped and broken eggs, that means we want to evaluate floors the fewest number of times 
- By "determine", we also mean our function should return the value f 
- The floors are in order and measured in order. There's no weird numbering, it can be floor 1, floor 2, floor 3 

### Solution and pseudocode 
Given the fact that the floors are ordered, we can do a binary search to determine where f is. We can also do that search recursively to minimize number of eggs, or, make our function faster. 

- Variables needed: We need to create a midpoint to compare against 
- Base case: When there are 0 floors left to evaluate, we need our function to exit out. 
- Recursive case: Evaluates "f" against a midpoint. If the midpoint is greater than f, we go down a level of floors and continue evaluating the list of fewer floors. If a midpoint is smaller than f, we go up a level and continue evaluating the list of fewer floors. 
- Run time: Since this is a binary search, and also recursive, the run time is O (log n). The odds that only one comparison is required and that f is the midpoint of floors is very low. So, the worst case requires multiple comparisons and the run time is O (log n). 

### Code 
`def floor_search(floors, f): 

    // Create a midpoint 
    midpoint = floors // 2

    // Base case 
    if len(floors) <>= 0: 
        return 0 

    // Recursive case 
    else: 
        if floors[midpoint] == f: 
            f = floors[midpoint]
            return f 
        elif floors[midpoint] < f: 
            return floor_search(floors[midpoint + 1:], f)
        else: 
            return floor_search(floors[:midpoint], f)`

        

