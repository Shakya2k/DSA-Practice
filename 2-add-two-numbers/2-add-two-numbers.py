# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def list_to_int(self,l):
        s = ""
        while l:
            s += str(l.val)
            l = l.next
        return int(s[::-1])
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = self.list_to_int(l1) + self.list_to_int(l2)
        result = str(result)
        answer = ListNode()
        c = []
        for i in result:
            c.append(ListNode(int(i)))
        c = c[::-1]
        for i in range (len(c)-1):
            c[i].next = c[i+1]
        return c[0]
            
        