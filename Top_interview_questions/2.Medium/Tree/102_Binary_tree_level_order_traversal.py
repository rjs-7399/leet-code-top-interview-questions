from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_order_traversal(root):
    q = deque([root])
    level_order = []
    while q:
        level = []
        for i in range(len(q)):
            current = q.popleft()
            level.append(current.val)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
        level_order.append(level)
    return level_order

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    ans = level_order_traversal(root)

    print(ans)