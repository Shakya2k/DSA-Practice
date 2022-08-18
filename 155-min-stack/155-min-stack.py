class MinStack(object):

    def __init__(self):
        self.minimum = 0
        self.stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if len(self.stack) == 1:
            self.minimum = self.stack[0]
        else:
            self.minimum = min(self.minimum, val)
        

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) == 0:
            print ("Stack Underflow")
        else:
            x = self.stack.pop()
            if x == self.minimum and len(self.stack) > 0:
                self.minimum = min(self.stack)
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minimum
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()