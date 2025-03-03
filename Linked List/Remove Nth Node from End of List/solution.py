# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = 0
        temp = head
        while temp:
            k += 1
            temp = temp.next

        target = k - n + 1
        prev = None
        curr = head
        for i in range(1, target):
            prev = curr
            curr = curr.next
        
        if prev == None:
            head = head.next
            return head

        prev.next = curr.next
        return head

        