"""class stack():
    def __init__(self):
        self.val = []
    def push_stack(self,v):
        self.val.append(v)
    def pop_stack(self):
        return self.val.pop()"""
        
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack =[]


        for i in range(len(s)):
            if s[i] !="]":
                stack.append(s[i])
            else:
            
                #for substring in []
                substr = ""
                while stack[-1]!= "[":
                    substr = stack.pop() + substr

                # for closing bracket
                stack.pop()

                # for digit outside of bracket
                k =""
                while stack and stack[-1].isdigit():
                    k= stack.pop() + k

                stack.append(int(k) * substr)


        return "".join(stack)
                
                
                
        