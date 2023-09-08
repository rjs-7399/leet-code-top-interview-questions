class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildTree_preorder_inorder(preorder, inorder):
    if inorder:
        index = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[index])
        root.left = buildTree_preorder_inorder(preorder, inorder[0:index])
        root.right = buildTree_preorder_inorder(preorder, inorder[index+1:])
        return root


if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    result_tree = buildTree_preorder_inorder(preorder, inorder)