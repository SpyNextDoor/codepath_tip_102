class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

x = Node(3)
y = Node(4)

x.next = y
print(x.value)