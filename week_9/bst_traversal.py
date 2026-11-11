
from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


# calculating the height of a tree

def height(root):
    if root is None:
        return 0

    return 1 + max(height(root.left), height(root.right))

def is_balanced(root):

    def check(node):
        if node is None:
            return 0

        left = check(node.left)
        if left == -1:
            return -1

        right = check(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1 

        return 1 + max(left, right)
    
    return check(root) != -1
