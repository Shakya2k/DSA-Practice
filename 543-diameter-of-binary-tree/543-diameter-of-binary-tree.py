# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return (-1, 0) # Height, diameter
            leftHeight, leftDiameter = dfs(node.left)
            rightHeight, rightDiameter = dfs(node.right)
            treeHeight = max(leftHeight, rightHeight) + 1
            treeDiameter = leftHeight + rightHeight + 2
            return treeHeight, max(leftDiameter, rightDiameter, treeDiameter)
        return dfs(root)[1]
        