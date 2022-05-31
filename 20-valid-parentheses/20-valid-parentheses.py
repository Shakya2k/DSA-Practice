class Solution:
    def stack_push(self, array, val):
        array.append(val)
    def stack_pop(self, array):
        del array[-1]
    def isValid(self, s: str) -> bool:
        stack = []
        L1 = [')','}',']']
        L2 = ['(','{','[']
        c = 0
        for i in range (len(s)):
            if stack == []:
                self.stack_push(stack,s[i])
                #print(stack)
                c+=1
            elif s[i] in L1:
                if stack[c-1] == L2[L1.index(s[i])]:
                    self.stack_pop(stack)
                    #print (stack)
                    c-=1
                else:
                    self.stack_push(stack, s[i])
                    #print (stack)
                    c+=1
            else:
                self.stack_push(stack, s[i])
                #print (stack)
                c+=1
        if len(stack)==0:
            return True
        else:
            return False
                