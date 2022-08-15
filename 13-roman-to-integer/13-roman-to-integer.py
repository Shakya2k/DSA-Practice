class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        relation = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        stack = []
        
        for i in range (len(s)-1, -1, -1):
            stack.append(s[i])
        
        store = 2**31
        total = 0
        
        for i in range (len(stack)):
            
            x = stack.pop()
            
            if relation[x] > store:
                
                total -= store
                total += (relation[x]-store)
            
            else:
                total += relation[x]
            
            store = relation[x]
        
        return total
                
            
                
            
        