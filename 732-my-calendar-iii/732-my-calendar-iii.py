class MyCalendarThree:

    def __init__(self):
        self.tmp=[]
        return None
        

    def book(self, start: int, end: int) -> int:
        bisect.insort(self.tmp,(start,1))
        bisect.insort(self.tmp,(end,-1))
        mx=0
        s=0
        for i in self.tmp:
            k1,k2 = i
            s+=k2
            mx = max(mx,s)
        return mx


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)