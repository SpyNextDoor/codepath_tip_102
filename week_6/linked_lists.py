"""
Unit 6: Session 1
Andre, Brian, Jean
"""
# 1.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# 2. 

"""
understand: 
given: list, a target score
output: count freq of the target score 

plan:
- initialize a count
- loop through the ll and if value at node equals
 target score, incremenet counter
"""

class Node:
    def __init__(self, house, score, next=None):
        self.house = house
        self.value = score
        self.next = next

def count_element(house_points, score):
    score_counter = 0

    curr_node = house_points

    while curr_node:
        if curr_node.value == score:
            score_counter += 1
        curr_node = curr_node.next
    return score_counter



house_points = Node("Gryffindor", 600, 
                Node("Ravenclaw", 300,
                    Node("Slytherin", 500,
                        Node("Hufflepuff", 600))))  
# print(count_element(house_points, 600))

# 3.

"""
understand:
- input: head of a linked list, type Node
- output: the middle Node
- edge case: list with one Node (return that Node); list with even Nodes (return the second middle Node)
Plan:
- two-pointer the technique
- move fast pointer by two, slow pointer by one
- if fast pointer is None, return the potion at the slow pointer's Node 
"""

class Node:
    def __init__(self, potion, next=None):
        self.potion = potion
        self.next = next

def find_middle_potion(potions):
    slowPtr = potions
    fastPtr = potions

    while fastPtr and fastPtr.next:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next

    return slowPtr.potion


potions1 = Node("Poison Antidote", Node("Shrinking Solution", Node("Trollblood Tincture")))
potions2 = Node("Elixir of Life", Node("Sleeping Draught", Node("Babbling Beverage", Node("Aging Potion"))))

print(find_middle_potion(potions1))
print(find_middle_potion(potions2))

# 4.
"""
understand: 
input: linked list output: linked list 
edge case: empty list, one node in the list

plan: save prev pointers and nodes, traverse through the linked list changing the pointers
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def reverse(events):
    prev = None
    current = events

    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev


events = Node("Potion Brewing", 
            Node("Spell Casting", 
                Node("Wand Making", 
                    Node("Dragon Taming", 
                        Node("Broomstick Flying")))))

print_linked_list(reverse(events))

# 5.

"""
understand:
given: head of a ll
output: boolean of whether the ll reads the same 
front to back or back to front
ie. palindrome with ll

plan: 
- reverse the given list
- traverse initial list and reversed list
    - compare values at each node
    - if any value is not equal then return false
    true otherwise
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def reverse(events):
    prev = None
    current = events

    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev

def is_mirrored(head):
    curr_node = head
    reversed_ll = reverse(head)

    while curr_node:
        if curr_node.value != reversed_ll.value:
            return False
        curr_node = curr_node.next
        reversed_ll = reversed_ll.next
    return True

list1 = Node("Phoenix", Node("Dragon", Node("Phoenix")))
list2 = Node("Werewolf", Node("Vampire", Node("Griffin")))

print(is_mirrored(list1))
print(is_mirrored(list2))

# 6.
"""
Understand:
- input: head of a ll
- output: node value if there's a cycle; otherwise, None
- edge cases: empty list (return None), a list with only one Node
Plan:
- two-pointer iteration, with a slow and fast pointer
- while iterating, if slow ever equals fast, then we return fast pointer's value
- otherwise, we return None at the end of the function
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def loop_start(path_start):
    slowPtr = path_start
    fastPtr = path_start

    while fastPtr and fastPtr.next:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next
        if slowPtr == fastPtr:
            return fastPtr.next.value
    
    return None

path_start = Node("Mystic Falls")
waypoint1 = Node("Troll's Bridge")
waypoint2 = Node("Elven Arbor")
waypoint3 = Node("Fairy Glade")

path_start.next = waypoint1
waypoint1.next = waypoint2
waypoint2.next = waypoint3
waypoint3.next = waypoint1

print(loop_start(path_start))
