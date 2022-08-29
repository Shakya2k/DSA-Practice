# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        res = root
        while not ((p.val < res.val and q.val > res.val) or (p.val > res.val and q.val < res.val)):
	        if res == p:
		        return p
	        if res == q:
		        return q

	        if p.val < res.val and q.val < res.val:
		        res = res.left
	        elif p.val > res.val and q.val > res.val:
		        res = res.right

        return res