class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def symmetric(root):
    def isMirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val == right.val and \
            isMirror(left.left, right.right) and \
            isMirror(left.right, right.left) :
            return True
        else:
            return False
    if not root:
        return True
    return isMirror(root.left, root.right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(44)

    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    ans = symmetric(root)
    print(ans)