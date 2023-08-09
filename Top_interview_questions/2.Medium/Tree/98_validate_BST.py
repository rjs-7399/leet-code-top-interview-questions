class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

tree_traversal = []

ans = True
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        tree_traversal.append(root.val)
        inorder_traversal(root.right)


if __name__ == "__main__":
    root = TreeNode(22)
    root.left = TreeNode(12)
    root.left.left = TreeNode(8)
    root.left.right = TreeNode(20)

    root.right = TreeNode(30)
    root.right.left = TreeNode(35)
    root.right.right = TreeNode(40)

    inorder_traversal(root)
    print(tree_traversal)
    length = len(tree_traversal)
    for i in range(length-1):
        if tree_traversal[i] >= tree_traversal[i+1]:
            print(False)
    print(True)