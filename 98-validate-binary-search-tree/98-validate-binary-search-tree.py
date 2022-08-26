# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.checkIfValid(root, -2**32, 2**32)
    
    def checkIfValid(self, root, minRange, maxRange):
        if not root:
            return True
        if minRange >= root.val or maxRange <= root.val:
            return False
        return self.checkIfValid(root.left, minRange, root.val) and self.checkIfValid(root.right, root.val, maxRange)
        