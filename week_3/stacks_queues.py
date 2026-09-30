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

# Q6.

# Q7.



