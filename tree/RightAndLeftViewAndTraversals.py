class Node(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


    def preorder(self):
        if(self.val == None):
            return

        print(self.val, end = " ")

        if(self.left):
           self.left.preorder()

        if(self.right):
            self.right.preorder()

    def inorder(self):
        if (self.val == None):
            return

        if (self.left):
            self.left.preorder()

        print(self.val, end = " ")

        if (self.right):
            self.right.preorder()

    def postorder(self):
        if (self.val == None):
            return

        if (self.left):
            self.left.preorder()

        if (self.right):
            self.right.preorder()

        print(self.val, end = " ")


    def leftView(self, root):
        self.leftViewUtil(root, 1, [0] )




    def leftViewUtil(self, root, level, max_level):
        if root == None:
            return

        if(level > max_level[0]):
            max_level[0] = level
            print(root.val , end = " " )

        self.leftViewUtil(root.left, level+1, max_level)
        self.leftViewUtil(root.right, level+1, max_level)

    def rightView(self, root):
        self.rightViewUtil(root, 1, [0])

    def rightViewUtil(self, root , level, max_level):
        if(root == None):
            return

        if(max_level[0] < level):
            print(root.val, end=" ")
            max_level[0]=level

        self.rightViewUtil(root.right, level+1, max_level)
        self.rightViewUtil(root.left, level+1, max_level)


if __name__ == '__main__':
    root = Node(1)
    root.right=Node(3)
    root.left=Node(2)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.left=Node(6)
    root.right.right=Node(7)
    root.right.right.right = Node(8)
    #root.preorder()
    print('Printing the left view of the tree', end = "\n")
    root.leftView(root)
    print("\n")
    print('Printing the right view of the tree', end = "\n")
    root.rightView(root)

