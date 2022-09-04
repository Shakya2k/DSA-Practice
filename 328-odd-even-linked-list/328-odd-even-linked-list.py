# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        odd = ListNode()
        even = ListNode()
        res = odd
        res_even = even
        
        count = 1
        track = head
        while track:
            if count % 2 != 0:
                odd.next = track
                odd = odd.next
                track = track.next
                count += 1
            else:
                even.next = track
                even = even.next
                track = track.next
                count += 1
            if not track:
                if count % 2 == 0:
                    even.next = None
                else:
                    odd.next = None

        
        odd.next = res_even.next
        return (res.next)
            
        