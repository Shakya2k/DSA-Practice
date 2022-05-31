# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Base case
        if not head:
            return False
        
        # We will move two pointers one at increment of 1 and one at increment of 2. If both 
        # collide we know there  is a cycle
        slow = head
        fast = head.next
        while fast != None and fast.next != None and slow != fast:
            slow = slow.next
            fast = fast.next.next
        if fast == None or fast.next == None:
            return False
        return True