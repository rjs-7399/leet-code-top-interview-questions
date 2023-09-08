class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def get_traversal(root):
    inorder_traversal = []
    def inorder(root):
        if root:
            inorder(root.left)
            inorder_traversal.append(root.val)
            inorder(root.right)
    inorder(root)
    return inorder_traversal

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right = TreeNode(4)

    index = 1
    inorder_traversal = get_traversal(root)
    print(inorder_traversal[index-1])