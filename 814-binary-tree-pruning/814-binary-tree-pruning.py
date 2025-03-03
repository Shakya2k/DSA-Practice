# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        return self._prune(root)
    
    @classmethod
    
    def _prune(cls, root: Optional[TreeNode]) -> Optional[TreeNode]:
	    if not root:
		    return None

	    root.left = cls._prune(root.left)
	    root.right = cls._prune(root.right)

	    return root if (root.val or root.left or root.right) else None
        