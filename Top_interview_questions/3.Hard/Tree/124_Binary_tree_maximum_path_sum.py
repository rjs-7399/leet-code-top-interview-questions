class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root):
        self.max_sum = float("-inf")
        self.dfs(root)
        return self.max_sum

    def dfs(self, node):
        if not node:
            return 0

        left_sum = max(0, self.dfs(node.left))
        right_sum = max(0, self.dfs(node.right))

        # Calculate the maximum path sum passing through the current node
        current_max_sum = node.val + left_sum + right_sum

        # Update the overall maximum path sum
        self.max_sum = max(self.max_sum, current_max_sum)

        # Return the maximum sum of a path starting from the current node
        return max(left_sum, right_sum) + node.val


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

    ans = Solution().maxPathSum(root)
    print(ans)
