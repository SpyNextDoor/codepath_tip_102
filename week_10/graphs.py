# Unit 10: Session 1

# 1.
"""
Plan:
- DFS


flights1 = [ [0, 1, 0], [0, 0, 1], [0, 0, 0] ]
             0          1            2

Location 0: [0, 1, 0]
           0  1  2
Location 1: [0, 0, 1]
            0  1  2
Location 2: [0, 0, 0]
"""
from collections import deque

def can_rebook1(flights, source, dest):
    search_stack = []
    visited = set()
    
    search_stack.append(source)
    while search_stack:
        current = search_stack.pop()
        if current not in visited:
            visited.add(current)
            if current == dest:
                return True
            for i in range(0, len(flights[current])):
                if flights[current][i] == 1:
                    search_stack.append(i)
    return False
    

flights1 = [
    [0, 1, 0], # Flight 0
    [0, 0, 1], # Flight 1
    [0, 0, 0]  # Flight 2
]

flights2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print(can_rebook1(flights1, 0, 2))
print(can_rebook1(flights2, 0, 2)) 


def can_rebook2(flights, source, dest):
    visited_nodes = set()
    queue = deque()
    
    queue.append(source)
    visited_nodes.add(source)
    
    while queue:
        current = queue.popleft()
        if current == dest:
            return True
        for i in range(0, len(flights[current])):
            if flights[current][i] == 1:
                queue.append(i)
    return False

print(can_rebook2(flights1, 0, 2))
print(can_rebook2(flights2, 0, 2)) 

                
    

