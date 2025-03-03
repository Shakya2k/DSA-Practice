# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderUtil(self,root):
        if root:
            return [root.val] + self.preorderUtil(root.left) + self.preorderUtil(root.right)
        else:
            return []
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = self.preorderUtil(root)
        return ans
    