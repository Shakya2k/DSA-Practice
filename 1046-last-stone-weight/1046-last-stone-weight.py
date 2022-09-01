class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) != 1:
            y = max(stones)
            stones.remove(y)
            x = max(stones)
            stones.remove(x)
            
            if x == y:
                pass
            stones.append(abs(y - x))
            
        if len(stones) == 1:
            print (stones)
        return stones[0]
        