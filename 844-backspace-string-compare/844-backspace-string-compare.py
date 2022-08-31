class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        
        for i in s:
            if i == "#" and len(stack_s) > 0:
                garbage = stack_s.pop()
            elif i != "#":
                stack_s.append(i)
                
        for i in t:
            if i == "#" and len(stack_t) > 0:
                garbage = stack_t.pop()
            elif i != "#":
                stack_t.append(i)
        #print (stack_s)
        #print (stack_t)
        if stack_s == stack_t:
            return True
        return False
                
        
        