# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderUtil(self, root):
        if root:
            return self.inorderUtil(root.left) + [root.val] + self.inorderUtil(root.right)
        else:
            return []
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = self.inorderUtil(root)
        return output