from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depth(root):
    if root is None:
        return 0
    depth_of_left_subtree = depth(root.left)
    depth_of_right_subtree = depth(root.right)
    return max(depth_of_left_subtree, depth_of_right_subtree)+1


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(99)

    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(100)

    ans = depth(root)
    print(ans)