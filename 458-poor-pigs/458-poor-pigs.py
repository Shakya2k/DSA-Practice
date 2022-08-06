class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        
        #importing the math module for callng the ceil and log funcions
        
        import math
        
        k = (minutesToTest//minutesToDie)
        if buckets < 2: return 0
        
        else:
            return int(math.ceil(math.log(buckets)/math.log(k+1)))
        
        