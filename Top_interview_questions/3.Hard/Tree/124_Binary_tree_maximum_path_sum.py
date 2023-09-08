class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def maxPathSum(root):
    max_sum = float("-inf")
    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0
        left_sum = max(dfs(node.left), 0)
        right_sum = max(dfs(node.right), 0)
        print("max sum : {}".format(max_sum))

        current_max_sum = node.val + left_sum + right_sum
        print("Current max sum : {}".format(current_max_sum))
        max_sum = max(max_sum, current_max_sum)
        return max(left_sum, right_sum) + node.val
    dfs(root)
    return max_sum





if __name__ == "__main__":
    root = TreeNode(-4)
    root.left = TreeNode(4)
    root.left.left = TreeNode(-2)
    root.left.right = TreeNode(-3)

    root.right = TreeNode(-5)
    root.right.right = TreeNode(3)

    root.right.right.left = TreeNode(1)
    root.right.right.left.left = TreeNode(6)
    root.right.right.left.right = TreeNode(7)

    root.right.right.right = TreeNode(8)
    root.right.right.right.left = TreeNode(9)
    root.right.right.right.right = TreeNode(10)

    ans = maxPathSum(root)
    print(ans)
