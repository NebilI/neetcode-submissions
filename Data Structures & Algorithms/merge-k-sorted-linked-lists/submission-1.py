# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:

            
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        heapq.heapify(min_heap)

        for i, head in enumerate(lists):

            if not head:
                continue
            heapq.heappush(min_heap, (head.val, i, head))
            lists[i] = head.next
            

        final_head = None
        curr = None
        while min_heap:

            val, index, head = heapq.heappop(min_heap)
            
            if final_head is None:
                final_head = curr = head
            else:
                curr.next = head
                curr = head

            curr.next = None
            
            if lists[index] is not None:
                heapq.heappush(min_heap, (lists[index].val, index, lists[index]))
                lists[index] = lists[index].next

            curr.next = None    
        
        return final_head
