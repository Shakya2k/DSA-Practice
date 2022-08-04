class Solution(object):
    def gcd(self, p, q):
        if q == 0:
            return abs(p)
        return self.gcd(q, p%q)
    
    def lcm(self, p, q):
        return (p*q//self.gcd(p,q))
    
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        L = self.lcm(p,q)
        
        if (L//q)%2 == 0:
            return 2
        return ((L//p)%2)
        
        
        
        