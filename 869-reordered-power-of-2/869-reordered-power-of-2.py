class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        
        def convert_to_list(x: int) -> list:
            x = str(x)
            res = []
            for i in x:
                res.append(int(i))
            res.sort()
            return res
        
        
        def power_list(x: int) -> list:
            temp = str(x)
            product = 1
            product_str = str(product)
            res = []
            
            while len(product_str) <= len(temp):
                res.append(product)
                product *= 2
                product_str = str(product)
            
            return res
        
        
        for i in power_list(n):
            if convert_to_list(n) == convert_to_list(i):
                return True
        return False
            
                
                
        
        
        