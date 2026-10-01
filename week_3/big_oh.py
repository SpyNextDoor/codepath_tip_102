# INSTRUCTOR DEMO
from collections import deque

def find_duplicates(arr):
    duplicates = []

    for i in range(len(arr)): #O(n)
        for j in range(i+1, len(arr)): #O(n)
            if arr[i] == arr[j]:
                if arr[i] not in duplicates: # O(n)
                    duplicates.append(arr[i])
    return duplicates

# space complex: O(n^3)

def find_duplicates_optimized(arr):
    duplicates = []
    seen = set()

    for num in arr: # O(n)
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)

    return duplicates

# PROBLEM SET 1

# 1. manage performance
# Unit 3: Session 1
# Andre, Jean, Brian

# Understand:
# Input: List of strings (each representing an action)
# Output: List of performance IDs (strings) that remain scheduled on the stage
# Plan: 
# Two stacks: the schedule and the canceled IDs
# Iterate through changes, and add scheduled IDs to the schedule stack
# Otherwise, push canceled IDs to the canceled stack
# If reschedule, pop from the canceled stack and push that to the schedule
# Return schedule


def manage_stage_changes(changes):
    schedule = []
    canceled = []

    for action in changes:
        if action.split()[0] == "Schedule":
            schedule.append(action.split()[1])
        elif action == "Cancel":
            if len(schedule) > 0:
                canceled.append(schedule.pop())
        else:
            if len(canceled) > 0:
                schedule.append(canceled.pop())
    
    return schedule

#  Space/ time: O(n)


# print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
# print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
# print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 


"""
Example Output:

["A", "C", "B", "D"]
[]
["Z"]

"""

# Understand:
# Input: tuple with prio and performance
# Output: list with higher prio first 
# Plan: 
#

def process_performance_requests(requests):
    requests.sort(reverse=True)
    result = []

    queue = deque(requests)

    while queue:
        priority, performance = queue.popleft()
        result.append(performance)
    return result

# time: O(nlogn), space: O(n)


# print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
# print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
# print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))


# 3. 


# Understand:
# Input: list of points at each booth
# Output: total number of points collected 
# Plan: - pop the list from the back to a summation
#       
#       - return the summation
#

def collect_festival_points(points):
    sum_of_points = 0

    while points:
        sum_of_points += points.pop()
    
    return sum_of_points
    
# space: O(1), time: O(n)

# print(collect_festival_points([2, 7, 4, 6])) 
# print(collect_festival_points([2, 7, 4, 6])) 
# print(collect_festival_points([1, 5, 9, 2, 8])) 

"""
26
19
25
"""

# 4. 

# Understand:
# Input: List that can contain integers and/or strings
# Output: List of integers of the visited booth numbers
# Edge case: If "back" on an empty stack, ignore it
# Plan:
# Make a stack of our visited booths
# Iterate through the clues list
# If we come across a number, append to the stack
# If it is "back," pop from the stack
# If there is nothing to pop, continue

def booth_navigation(clues):
    visited = []

    for clue in clues:
        if clue == "back":
            if visited:
                visited.pop()
        else:
            visited.append(clue)

    return visited

clues = [1, 2, "back", 3, 4]
print(booth_navigation(clues)) 

clues = [5, 3, 2, "back", "back", 7]
print(booth_navigation(clues)) 

clues = [1, "back", 2, "back", "back", 3]
print(booth_navigation(clues))

# T

