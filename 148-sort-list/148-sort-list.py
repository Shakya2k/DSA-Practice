# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        cur = head
        d = {-1:ListNode()}
        index = 0
        while cur:
            d[index] = cur
            d[index-1].next = d[index]
            cur = cur.next
            index += 1
        return self.mergeSort(d, 0, len(d)-2)
    
    def mergeSort(self, d, low, high):
        if low < high:
            mid = (low+high)//2
            left = self.mergeSort(d, low, mid)
            right = self.mergeSort(d, mid+1, high)

            head = ListNode()
            cur = head
            while left and right:
                if left.val <= right.val:
                    cur.next = left
                    left = left.next
                else:
                    cur.next = right
                    right = right.next
                cur = cur.next

            while left:
                cur.next = left
                left = left.next
                cur = cur.next
            while right:
                cur.next = right
                right = right.next
                cur = cur.next
            cur.next = None
            return head.next
        d[low].next = None
        return d[low]