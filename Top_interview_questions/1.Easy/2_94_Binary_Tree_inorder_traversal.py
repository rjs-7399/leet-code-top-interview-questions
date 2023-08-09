class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

result = []
def inorder(root):
    if root:
        inorder(root.left)
        result.append(root.val)
        inorder(root.right)
    return result

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    ans = inorder(root)
    print(ans)