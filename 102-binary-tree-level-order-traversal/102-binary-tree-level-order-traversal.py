# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        # Take an early exit if root is None
        if not root:
            return None
        
        #Recursion
        def helper(node,level):
            # Check if new list has to be created or not
            # If the sublist are equal to the level we are parsing, then add a new sublist
            if len(levels) == level:
                levels.append([])
            
            # Append the node to the corresponding level's sublist
            levels[level].append(node.val)
            # Check if it has left and right child, if it does, recursively call on them with level + 1
            if node.left:
                helper(node.left,level+1)
            if node.right:
                helper(node.right,level+1)
            
            return levels
            
        return helper(root,0) 