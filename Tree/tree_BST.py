class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
    
    #INSERTION
    def insert(root, value):
        if (root == None):
            return Node(value)
        if(root.data == value):
            return root
        if(root.data > value):
            root.left = Node.insert(root.left, value)
        else:
            root.right = Node.insert(root.right, value)
        return root

def InOrder(root):
    if (root != None):
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)

root = Node(20)
root.left = Node(15)
root.right = Node(30)
root.left.left = Node(12)
root.left.right = Node(18)
