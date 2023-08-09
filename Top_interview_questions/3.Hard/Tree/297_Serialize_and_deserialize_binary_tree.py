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

def serialize_tree(input_node):
    result = []
    def serialize(node):
        if node:
            result.append(node.val)
            serialize(node.left)
            serialize(node.right)
        else:
            result.append('#')
        return ",".join(str(elem) for elem in result)
    return serialize(input_node)

def deserialize_tree(arr, index):
    if arr[index] == "#":
        return None
    node = TreeNode(int(arr[index]))
    index += 1
    node.left = deserialize_tree(arr, index)
    index += 1
    node.right = deserialize_tree(arr, index)
    return root


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)


    tree_traversal = serialize_tree(root)

    print(tree_traversal)
    print("Inorder traversal : ")

    tree_traversal = tree_traversal.split(",")

    result_tree = deserialize_tree(tree_traversal, 0)
    inorder(result_tree)
