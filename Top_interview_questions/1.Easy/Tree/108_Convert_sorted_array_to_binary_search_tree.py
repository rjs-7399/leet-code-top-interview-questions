class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def array_to_tree(arr):
    if not arr:
        return None
    mid = len(arr)//2
    root = TreeNode(arr[mid])
    root.left = array_to_tree(arr[:mid])
    root.right = array_to_tree(arr[mid+1:])
    return root


if __name__ == "__main__":
    arr = [1,2,3]
    root = array_to_tree(arr)
    inorder(root)