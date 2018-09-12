class Node(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def minDepth(self, root):
        q = []
        if root is None:
            return 0
        q_cur = []
        depth = 0
        q.append(root)
        while len(q) > 0:
            cur = q.pop()
            if cur.left is not None:
                q_cur.append(cur.left)
            if cur.right is not None:
                q_cur.append(cur.right)

            if len(q) == 0:
                depth += 1
                q.extend(q_cur)
                q_cur = []

            if cur.left is None and cur.right is None:
                return depth


if __name__ == ' __main__' :
    # [3,9,20,null,null,15,7]
    s = Solution()
    root = Node(3)
    root.left = Node(20)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(7)
    min_depth = s.minDepth(root)
    print('min depth of the tree: ', min_depth)
