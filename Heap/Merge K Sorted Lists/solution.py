# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or lists == [] or len(lists) == 0:
            return None

        dummy = ListNode()
        tail = dummy

        h = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(h, (node.val, i, node))
        
        while len(h) > 0:
            min_val, index, curr_node = heapq.heappop(h)
            tail.next = curr_node
            tail = curr_node
            curr_node = curr_node.next

            if curr_node:
                heapq.heappush(h, (curr_node.val, index, curr_node))
        
        return dummy.next
        