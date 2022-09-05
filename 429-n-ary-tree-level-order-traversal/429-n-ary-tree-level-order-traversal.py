"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if(root == None):
            return []
      
        op =[]
        nodeToTraverse= [root]
      
        while(len(nodeToTraverse)>0):
            n = len(nodeToTraverse)
            op.append([])
        
            for i in range(n):
                node = nodeToTraverse.pop(0)
                if(node != None):
                    op[-1].append(node.val)
            
                    for child in node.children:
                        nodeToTraverse.append(child)
        return op
        
        
        