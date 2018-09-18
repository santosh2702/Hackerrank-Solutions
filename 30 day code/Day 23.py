class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if not root:
            return Node(data)
        else:
            if data <= root.data:
                current = self.insert(root.left, data)
                root.left = current
            else:
                current = self.insert(root.right, data)
                root.right = current
        return root

    def levelOrder(self, root):
        queue = [root]
        while len(queue) is not 0:
            curr = queue[0]
            queue = queue[1:]
            print(str(curr.data) + " ", end="")

            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
