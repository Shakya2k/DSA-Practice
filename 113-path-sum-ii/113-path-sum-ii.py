# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root, total, path):
            if not root:
                return

            if total + root.val == targetSum and not root.right and not root.left:
                res.append(path + [root.val])
                return
        
            if root.left:
                dfs(root.left, total + root.val, path + [root.val])
                
            if root.right:
                dfs(root.right, total + root.val, path + [root.val])
         
        res = []
		
        dfs(root, 0, [])
        return res