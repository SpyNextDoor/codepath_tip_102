"""
Unit 4: Session 2
Andre, Brian, Jean
"""

# 1.
"""
Understand:
- Input: List of integers; integer
- Output: Boolean
- Edge cases: Empty list, list one value
Plan:
- Iterate through the list
- If the available time - current number is in the set, return True
- Add it to a set
- Iterated through without finding a pair = return False

"""


def find_task_pair(task_times, available_time):
    time_set = set()
    for current_elt in task_times:
        if available_time - current_elt in time_set:
            return True
        time_set.add(current_elt)
    
    return False


task_times = [30, 45, 60, 90, 120]
available_time = 105
print(find_task_pair(task_times, available_time))

task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
print(find_task_pair(task_times_2, available_time))

task_times_3 = [20, 30, 50, 70]
available_time = 60
print(find_task_pair(task_times_3, available_time))

# O(n) time and space


# 2.
""""
Understand:
- Input: a list of tuples (start, end)
- Output: smallest in minutes 
- Edge cases: - empty list, a list of with one tuple
Plan:
- initialize a small_gap variable to inf
- iterate through the list 
    - diff: (_, end) - (start, _) < small_gap
    - small_gap = diff
return small_gap
space - O(1)
time - O(n)
"""

def find_smallest_gap(work_sessions):
    if len(work_sessions) <= 1:
        return 0

    small_gap = float("inf")
    for i in range(1, len(work_sessions)):
        prevEnd = (work_sessions[i - 1][1]//100 * 60) + work_sessions[i - 1][1]%100
        currStart = (work_sessions[i][0]//100 * 60) + work_sessions[i][0]%100
        diff = currStart - prevEnd

        if diff < small_gap:
            small_gap = diff
    
    hours, minutes = divmod(small_gap, 100)

    return (hours * 60) + minutes


work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
print(find_smallest_gap(work_sessions))

work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
print(find_smallest_gap(work_sessions_2))

work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
print(find_smallest_gap(work_sessions_3))


















#3. 