# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        len_list = 0
        temp = head
        while temp != None:
            len_list += 1
            temp = temp.next
        try:
            for _ in range(k % len_list):
                temp = head
                while temp.next.next != None:
                    temp = temp.next
                n = temp.next
                temp.next = None
                n.next = head
                head = n
            return head
        except ZeroDivisionError:
            return ListNode("")