# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        leftnode = self.lowestCommonAncestor(root.left, p, q)
        rightnode = self.lowestCommonAncestor(root.right, p, q)
        if leftnode and rightnode: # p and q are from decendants
            return root
        elif leftnode or rightnode: # only found one from decendants 
            if root.val == p.val or root.val == q.val:
                return root
            elif leftnode:
                return leftnode
            return rightnode
        elif root.val == p.val:
            return p
        elif root.val == q.val:
            return q
        return None