from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def zig_zag_level_order(root):
    if root:
        q = deque([root])
        level_order = []
        index = 0
        while q:
            level = []
            for i in range(len(q)):
                current = q.popleft()
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
                level.append(current.val)
            if index%2 == 0:
                level_order.append(level)
            else:
                level_order.append(level[::-1])
            index += 1
            print(index)
        return level_order
    else:
        return []

if __name__ == "__main__":
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    ans = zig_zag_level_order(root)
    print(ans)