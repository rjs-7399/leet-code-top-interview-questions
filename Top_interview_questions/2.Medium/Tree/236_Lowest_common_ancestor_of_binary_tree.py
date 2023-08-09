class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    def find_path_to_node(root, target):
        if root:
            stack = [(root, [root.val])]
            all_paths = []
            while stack:
                node, path = stack.pop()

                if node.val == target:
                    all_paths.append(path)

                if node.right:
                    stack.append((node.right, path + [node.right.val]))
                if node.left:
                    stack.append((node.left, path + [node.left.val]))
            return all_paths
    p_path = find_path_to_node(root, p.val)
    q_path = find_path_to_node(root, q.val)
    if len(p_path)<1 or len(q_path)<1:
        return TreeNode(None)
    else:
        if len(p_path) < len(q_path):
            ans = [elem for elem in p_path[0] if elem in q_path[0]]
        else:
            ans = [elem for elem in q_path[0] if elem in p_path[0]]
        return TreeNode(ans[-1])

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

    p = TreeNode(5)
    q = TreeNode(1)
    ans = lowestCommonAncestor(root, p, q)
    print(ans.val)