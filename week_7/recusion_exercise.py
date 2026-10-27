"""
Unit 7: Session 1
"""

# 1.
"""
Understand:
- Input: list of strings
- Output: int count of list length
Iterative Plan:
- iterate, increment count; return count
Recursive Plan:
- check if list is empty --> return 0
- return 1 + recursive_call(sliced list)
"""

def count_suits_iterative(suits):
    count = 0
    for suit in suits:
        count += 1
    return count

def count_suits_recursive(suits):
    if len(suits) == 0:
        return 0
    return 1 + count_suits_recursive(suits[1:])

# print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark II", "Mark III"]))

# 2. 
"""
Understand: 
- Input: list
- Output: int 

Plan:
use recursion
"""

"""def sum_stones(stones):
    if not stones:
        return 0
    
    return stones[0] + sum_stones(stones[1:])


print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))"""


# 3.
"""
understand: list input
output: total number of distinct suits --> int

plan:
iterative:
    - create an empty set
    - iterative: loop through adding elts in the set if an elt is already in the set we don't add it
    - return the length of the set

recursive:
    - if len(lst) == 0 return 0
    - if len(lst) == 1 return 1
    - otherwise:    
        - 
    
"""

def count_suits_iterative(suits):
    unique_suits = set()

    for suit in suits:
        if suit not in unique_suits:
            unique_suits.add(suit)
    return len(unique_suits)

def count_suits_recursive(suits):
    if len(suits) == 0:
        return 0
    
    current_suit = suits[0]
    rest_suit = suits[1:]
    
    if current_suit not in rest_suit:
        return 1 + count_suits_recursive(rest_suit)
    else:
        return count_suits_recursive(rest_suit)
        

print(count_suits_iterative(["Mark I", "Mark I", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))
    
    
# 4.
"""
Understand:
- input: int
- output: int
Plan:
- Check our base cases: input = 0 -> return 0; input = 1 -> return 1
- Otherwise, return function(n - 1) + function(n - 2)
"""

def fibonacci_growth(n):
    if n == 0 or n == 1:
        return n
    return fibonacci_growth(n - 1) + fibonacci_growth(n - 2)

print(fibonacci_growth(5))
print(fibonacci_growth(8))

# 5.
"""
Understand:
- input: int
- output: int (power of 4)

Plan:
- check our base cases
- use recursion 
"""

def power_of_four(n):
    if n == 0:
        return 1

    if n < 0:
        return .25 * power_of_four(n + 1)
    else:
        return 4 * power_of_four(n - 1)


print(power_of_four(2))
print(power_of_four(-2))
    
    

