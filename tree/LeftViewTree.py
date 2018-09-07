class Node(object):
    def __init__(self, v):
        self.value = v
        self.right = None
        self.left = None

    def leftView(self):
        q= []
        if self.value !=None:
            q.append(self)

        self.leftViewUtil(q)

    def leftViewUtil(self, q):
        le = int(len(q))
        q1 = []
        flag = False
        if(le ==0):
            return
        while(le > 0 ):
            cur = q.pop()
            if(not flag):
                print(cur.value)
                flag=True
            if(cur.left!=None):
                q1.append(cur.left)
            if(cur.right):
                q1.append(cur.right)
            le = le-1

        self.leftViewUtil(q1)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right=Node(5)
    root.leftView();
