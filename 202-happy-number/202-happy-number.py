class Solution:
    def isHappy(self, n: int) -> bool:
        store = []
        def happy(s):
            sum1 = 0
            for i in s:
                sum1 += int(i)**2
            return sum1
        
        x = n
        while x != 1:
            x = happy(str(x))
            if x == 1:
                return True
            elif x not in store:
                store.append(x)
            else:
                return False
            
        return True
            
            
            
        
        
            
        