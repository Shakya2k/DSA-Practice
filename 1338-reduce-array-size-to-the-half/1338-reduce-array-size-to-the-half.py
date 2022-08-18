class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        #print(unique)
        occurences = Counter(arr)
        
        #print(occurences)
        res = 0
        add = 0
        values = occurences.values()
        values.sort()
        values = values[::-1]
        #print(occurences)
        
        for val in values:
            res += 1
            if add + val >= len(arr)//2:
                return res
            add += val

        #print (res)
            
        
        
        
            
        
        