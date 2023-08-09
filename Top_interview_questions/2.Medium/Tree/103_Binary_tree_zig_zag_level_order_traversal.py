from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def zigZagLevelOrder(root):
    if root:
        result = []
        q = deque([root])
        length = 0
        while q:
            length+=1
            level = []
            for index in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if length%2 != 0:
                result.append(level)
            else:
                level.reverse()
                result.append(level)
        return result
    else:
        return []


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)

    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    result = zigZagLevelOrder(root)
    print(result)