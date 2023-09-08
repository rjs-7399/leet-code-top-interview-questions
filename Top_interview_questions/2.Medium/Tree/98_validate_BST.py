class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def get_inorder(root):
    traversal = []
    def inorder(root):
        if root:
            inorder(root.left)
            traversal.append(root.val)
            inorder(root.right)
    inorder(root)
    for i in range(len(traversal)-1):
        if traversal[i] >= traversal[i+1]:
            return False
    return True

if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    traversal = get_inorder(root)
    print(traversal)
