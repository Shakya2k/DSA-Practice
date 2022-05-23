# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def findNode(head,n):
            slow = fast = head

            #find the nth node from the end:
            for i in range(n):
                fast = fast.next

            while fast != None:
                slow = slow.next
                fast = fast.next
            return slow
        
        dummy = ListNode(-1)
        dummy.next = head
        
        x = findNode(dummy, n+1)
        x.next = x.next.next
        
        return dummy.next