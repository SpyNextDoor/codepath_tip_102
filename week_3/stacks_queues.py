from collections import deque

stack = []

stack.append(1)
stack.append(2)
stack.append(3)

# print(stack)
# print(stack[-1])

popped = stack.pop()

# print(popped)
# print(stack)

popped = stack.pop()
popped = stack.pop()

# print(stack)

# popped = stack.pop()
# always check for empty stack before you pop


# QUEUE

queue = deque()

queue.append("Messi")
queue.append("R9")
queue.append("kaka")

# print(queue.popleft())
# print(queue.popleft())



# INSTRUCTOR DEMO: correct paranthesis order

# Unit 3: Session 1

# Q.2

# Understand: 
# Input: list of strings
# Output: list of strings, reversing the input
# Edge cases: empty list, one comment

# Plan:
# create an empty stack
# Iterate through the "queue" starting from the end
# Append each comment to our stack
# Return that stack

def reverse_comments_queue(comments):
    if len(comments) <= 1:
        return comments
    
    stack = []
    for i in range(len(comments) - 1, -1, -1):
        stack.append(comments[i])

    return stack

# Q4.

#PROBLEM SET VRSION 1
"""
Understand:
Input:string
Output: boolean indicating symmetry
Edge cases:string is empty, string has one character

Plan:
1. First check edge cases
2. Set two pointers to the string. One pointer to 
the front and the other at the end
3. Use a while loop until left >= right
"""

def is_symmetrical_title(title):
    title = title.strip(" ,.!?").lower()
    
    if len(title) == 0:
        return False
    if len(title) == 1:
        return True
    
    pointer1, pointer2 = 0, len(title) - 1
    while pointer1 < pointer2:
        if title[pointer1].isalnum() and title[pointer2].isalnum():
            if title[pointer1] != title[pointer2]:
                return False
            
            pointer1 += 1
            pointer2 -= 1
        else:
            if not title[pointer1].isalnum():
                pointer1 += 1
            if not title[pointer2].isalnum():
                pointer2 -= 1
    
    return True

# print(is_symmetrical_title("A Sa.nta at NASA"))
# print(is_symmetrical_title("Social Media")) 
                                

# Q5.
"""
input: two strings each character representing an event
output: merge both lists in alternating order
edge case: one list empty?

plan:
- use two pointers: pointer1 in lst1 same as lst2
- initialize the pointers and a merged_schedule lst
- for each elt append the elt in each lst and increment pointer 

"""

def merge_schedules(schdl_1, schdl_2):
    p_1 = 0
    p_2 = 0
    merged_schdl = ""

    while p_1 < len(schdl_1) or p_2 < len(schdl_2):
        if p_1 < len(schdl_1):
            merged_schdl += schdl_1[p_1]
            p_1 += 1

        if p_2 < len(schdl_2):
            merged_schdl += schdl_2[p_2]
            p_2 += 1

    return merged_schdl

# print(merge_schedules("abc", "pqr")) 
# print(merge_schedules("ab", "pqrs")) 
# print(merge_schedules("abcd", "pq")) 


# Q6.

# Q7.

# hackerrank exercises:

def mystery(nums):
    left = len(nums) - 1
    right = len(nums) - 1

    while right >= 0:
        if nums[right] != 0:
            temp = nums[right]
            nums[right] = nums[left]
            nums[left] = temp
            left -= 1
        right -= 1
    return nums 

# print(mystery([0, 0, 1, 2, 0, 3]))

def two_sum(numbers, target):
    # Write your code here
    if len(numbers) < 2:
        return None
    
    pointer_1 = 0
    pointer_2 = len(numbers) - 1
    
    while len(numbers) > 0:
        if numbers[pointer_1] + numbers[pointer_2] > target:
            pointer_2 -= 1
        else:
            pointer_1 += 1

    return None

numbers = [2, 7, 11, 15]
print(two_sum(numbers, 9))



