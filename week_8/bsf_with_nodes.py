class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# INSERTION

def insert(root, val):
    if root is None:
        return TreeNode(val)

    if val < root.val: 
        root.left = insert(root.left, val) # go left
    else:
        root.right = insert(root.right, val) # go right

    return root

root = None
for val in [5, 3, 7, 1, 4, 6, 9]:
    root = insert(root, val)

# left print right --> in-order (sorted)
# print left right --> pre-order
# left right print --> post-order

def in_order_traversal(root): 
    if root is None:
        return []

    return [in_order_traversal(root.left)] + [root.val] + [in_order_traversal(root.right)]

# print(in_order_traversal(root))

# DELETION

#cases:
# - no children --> assign node to null
# - one child --> swap and delete
# - two children --> reprace the intended node with its order successor and delete it. 

# exercises

from collections import deque

"""
Unit 8: Session 1
"""

# 1.
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)


root = TreeNode("Poseidon", TreeNode("Atlantis", TreeNode("Coral"), TreeNode("Pearl")), TreeNode("Oceania", TreeNode("Kelp"), TreeNode("Reef")))
print_tree(root)

# 2.
"""
understand:
given: a binary tree, roo, l child, r child
output: boolean true/false lchild.val == rchild.val
edge: no root, root has no children

plan: check the right and the left nodes 
"""

def mertwins(root):
    if not root or not root.left or not root.right:
        return False

    return root.left.val == root.right.val

"""
      Mermother
       /    \
    Coral   Coral
"""
root1 = TreeNode("Mermother", TreeNode("Coral"), TreeNode("Coral"))

"""
      Merpapa
       /    \
   Calypso  Coral
"""
root2 = TreeNode("Merpapa", TreeNode("Calypso"), TreeNode("Coral"))

"""
      Merenby
           \    
         Calypso  
"""
root3 = TreeNode("Merenby", None, TreeNode("Calypso"))

print(mertwins(root1))
print(mertwins(root2))
print(mertwins(root3))



# 3. 

"""
Understand: a binary search tree with non leaf nodes as AND or OR, leaf nodes are True or False, return a boolean
edge cases: empty root, no children 


plan: check if the node has no children, return root.val
if left and right does exist, get the left and right values

check the conditions of the left and right values and return it 
"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def get_decision(root):
    if not root:
        return False

    if not root.left and not root.right:
        return root.val

    left = get_decision(root.left)
    right = get_decision(root.right)

    if root.val == "AND":
        return left and right
    else: 
        return left or right

"""
        OR
      /    \
    True  False
"""
expression1 = TreeNode("OR", TreeNode(True), TreeNode(False))

"""
       False
"""
expression2 = TreeNode(False)

"""
       OR
     /    \
   False  AND
        /     \
       True    True
"""
expression3 = TreeNode("OR", TreeNode(False), TreeNode("And", TreeNode(True), TreeNode(True)))


print(get_decision(expression1))
print(get_decision(expression2))
print(get_decision(expression3))


expression1 = TreeNode("OR", TreeNode(True), TreeNode(False))
expression2 = TreeNode(False)


# 4.
"""
Understand:
- Input: TreeNode (root for a Binary Search Tree)
- Output: Array of strings
- Edge cases: no root, no node, no children
Plan:
- Recursion
- Base case: no left child, so return the value but in a list format
- Just keep going left if the left child exists
- return the value of the current node we're on in a list + the recursive call
"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
"""
def leftmost_path(root):
    if root is None:
        return []

    return [ root.val ] + leftmost_path(root.left)
"""

"""
        CaveA
       /      \
    CaveB    CaveC
    /   \        \
CaveD CaveE     CaveF  
"""
system_a = TreeNode("CaveA", 
                  TreeNode("CaveB", TreeNode("CaveD"), TreeNode("CaveE")), 
                          TreeNode("CaveC", None, TreeNode("CaveF")))

"""
  CaveA
      \
      CaveB
        \
        CaveC  
"""
system_b = TreeNode("CaveA", None, TreeNode("CaveB", None, TreeNode("CaveC")))



# 5.

"""
Understand:
- Input: TreeNode (root for a Binary Search Tree)
- Output: Array of strings
- Edge cases: no root, no node, no children
plan:
create a list
loop through the left path with a while loop
keep adding left node values
"""

def leftmost_path(root):
    vals = []
    if not root:
        return vals
    curr = root
    while curr:
        vals.append(curr.val)
        curr = curr.left
    return vals


print(leftmost_path(system_a))
print(leftmost_path(system_b))