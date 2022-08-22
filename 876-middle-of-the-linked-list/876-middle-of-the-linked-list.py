# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        store = {}
        i = 0
        while head:
            store[i] = head
            i += 1
            head = head.next
        return store[len(store)//2]