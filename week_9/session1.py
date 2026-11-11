# Unit 9: Session 1
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



# 1.
"""
U:
- input: 2 root nodes
- output: boolean
- edge cases: either root node is None
P:
- recursive preorder traversal through the trees
- compare:
-    if both are None, return True
-    if only one of them is None, return False
-    if both exist but their values are different, return False
-    if both exist and their values are the same, return True
"""
def is_clone(guest1, guest2):
    if guest1 is None and guest2 is None:
        return True
    elif guest1 is None or guest2 is None:
        return False
    else:
        return (guest1.val == guest2.val) and is_clone(guest1.left, guest2.left) and is_clone(guest1.right, guest2.right)

"""
     John Doe               John Doe
     /      \             /       \
  6 ft    Brown Eyes      6ft      Brown Eyes
"""
guest1 = TreeNode("John Doe", TreeNode("6 ft"), TreeNode("Brown Eyes"))
guest2 = TreeNode("John Doe", TreeNode("6 ft"), TreeNode("Brown Eyes"))

"""
     John Doe         John Doe
     /                       \
   6 ft                     6 ft
"""
guest3 = TreeNode("John Doe", TreeNode("6 ft"))
guest4 = TreeNode("John Doe", None, TreeNode("6 ft"))

print(is_clone(guest1, guest2))
print(is_clone(guest3, guest4))


#2
"""
U: 
given: hotel node
output: list of hotel room --> values at each node
edge case: hotel note is None return []

P:
left -> right 
- create a empty list
- initialize the queue with root
- 
"""


class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def map_hotel(hotel):
    if not hotel:
        return []
    
    num_rooms = []
    queue = deque([hotel])
    while queue:
        hotel_room = queue.popleft()
        num_rooms.append(hotel_room.val)

        if hotel_room.left:
            queue.append(hotel_room.left)

        if hotel_room.right:
            queue.append(hotel_room.right)
    return num_rooms

hotel = TreeNode("Lobby", 
                TreeNode(101, TreeNode(201, TreeNode(301)), TreeNode(202)),
                TreeNode(102, TreeNode(203), TreeNode(204, None, TreeNode(302))))

print(map_hotel(hotel))


# 3.
"""
U: 
given: door root
output: min depth of the tree
edge case: empty door 

P:
base case: if node is none, return 0
use recursion, get the height of the left and right subtree
"""


def min_depth(door):
    if not door:
        return 0

    left = min_depth(door.left)
    right = min_depth(door.right)

    return 1 + min(left, right)

"""
     Door
    /    \
 Attic    Cursed Room
         /       \
      Crypt     Haunted Cellar
"""

door = TreeNode("Door", TreeNode("Attic"), TreeNode("Cursed Room", TreeNode("Crypt"), TreeNode("Haunted Cellar")))

print(min_depth(door))


# 4.
def min_depth(door):
    if not door:
        return []
        
    queue = deque([(door, 1)])
    while queue:
        hotel_room,depth = queue.popleft()

        if hotel_room.left:
            queue.append(hotel_room.left )

        if hotel_room.right:
            queue.append(hotel_room.right)

    # TODO: