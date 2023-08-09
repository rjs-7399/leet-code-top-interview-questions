class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def kthSmallest(root, k):
    tree_traversal = []
    def inorder_traversal(root):
        if root:
            inorder_traversal(root.left)
            tree_traversal.append(root.val)
            inorder_traversal(root.right)

    inorder_traversal(root)
    tree_traversal.sort()
    return tree_traversal[k - 1]

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(1)

    root.right = TreeNode(6)
    root.left.right = TreeNode(4)

    k = 2
    ans = kthSmallest(root, 2)
    print(ans)