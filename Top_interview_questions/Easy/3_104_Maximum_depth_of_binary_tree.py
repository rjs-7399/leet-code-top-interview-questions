class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def depth(root):
    if root is None:
        return 0
    return max(depth(root.left), depth(root.right)) + 1


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    ans = depth(root)
    print(ans)