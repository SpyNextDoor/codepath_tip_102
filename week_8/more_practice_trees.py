"""
Unit 8: Session 2
"""

# 1.
"""
U:
- input: node
- output: int
- edge cases: no node, one node, any node that has missing children
P:
- Recursion to traverse through the BST
- inorder traversal
- for a node: if its value is odd, return 1; otherwise, return 0
- recrusive calls to add everything together
"""

from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

"""def count_odd_splits(root):
    if not root:
        return 0

    sum = 0
    if root.val % 2 != 0:
        sum += 1
    return sum + count_odd_splits(root.left) + count_odd_splits(root.right)

values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)"""

# print(count_odd_splits(monstera))
# print(count_odd_splits(None))

# 2.
"""
u: given the root of the tree, 
output: boolean (T or F)
edge cases: empty root

P:
use recursion to see if the curr node is equal to the target name

"""

def find_flower(inventory, name):
    if not inventory:
        return False

    if inventory.val == name:
        return True
    elif name < inventory.val:
        return find_flower(inventory.left, name)
    else:
        return find_flower(inventory.right, name)


"""
         Rose
        /    \
      Lilac   Tulip
     /  \       \
  Daisy  Lily  Violet
"""

# using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]

garden = build_tree(values)

# print(find_flower(garden, "Lilac"))  
# print(find_flower(garden, "Sunflower")) 

# 3.
def non_bst_find_flower(root, name):
    if root is None:
        return False
    
    if root.val == name:
        return True

    return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)

"""
                Daisy
                /    \
            Lily   Tulip
            /  \       \
        Rose  Violet  Lilac
"""

# using build_tree() function at top of page
values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)

# print(non_bst_find_flower(garden, "Lilac"))  
# print(non_bst_find_flower(garden, "Sunflower"))  

