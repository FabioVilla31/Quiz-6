
# This code is contributed by Bhavya Jain



class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

# A utility function to insert a new node with the given key
def insertar(root,node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insertar(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insertar(root.left, node)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def minValueNode(node):
    current = node

    # loop down to find the leftmost leaf
    while (current.left is not None):
        current = current.left

    return current

def deleteNode(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif (key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root

# A function to do inorder tree traversal
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val),
        printInorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val),

def printPreorder(root):
    if root:
        print(root.val),
        printPreorder(root.left)
        printPreorder(root.right)

def buscar(root,key):
    if root is None or root.val == key:
        return root.val
    if root.val < key:
        return buscar(root.right, key)
    else:
        return buscar(root.left, key)


def minValue(node):
    current = node
    while (current.left is not None):
        current = current.left
    return current.val
def maxValue(node):
    current = node
    while (current.right is not None):
        current = current.right
    return current.val


r = Node(55)
insertar(r, Node(32))
insertar(r, Node(22))
insertar(r, Node(40))
insertar(r, Node(76))
insertar(r, Node(69))
insertar(r, Node(85))
insertar(r, Node(100))
insertar(r, Node(12))
insertar(r, Node(89))
insertar(r, Node(45))
insertar(r, Node(200))

print ("PreOrden")
printPreorder(r)

print ("\nInOrden")
printInorder(r)

print ("\nPostOrden")
printPostorder(r)

print ("\nMinimum value is %d" %(minValue(r)))
print ("\nMaximum value is %d" %(maxValue(r)))

print ("\nThe value you're looking for was found and is: %d" %(buscar(r,76)))


print ("\nThe tree printed in order")
inorder(r)

#print ("\nDelete 200")
#root = deleteNode(r, 200)
#print ("Inorder traversal of the modified tree")
#inorder(r)

#print ("\nDelete 32")
#root = deleteNode(r, 32)
#print ("Inorder traversal of the modified tree")
#inorder(r)

#print("\nDelete 89")
#root = deleteNode(r, 89)
#print("Inorder traversal of the modified tree")
#inorder(r)