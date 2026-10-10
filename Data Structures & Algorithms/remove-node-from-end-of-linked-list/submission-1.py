# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def len_list(self, head):
        length = 0
        curr = head

        while curr is not None:
            curr = curr.next
            length += 1
        
        return length

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        to_traverse = self.len_list(head) - n
        prev = None
        curr = head

        while curr is not None:
            if to_traverse == 0:
                if prev is not None:
                    prev.next = curr.next
                    return head
                else:
                    return curr.next
            
            prev = curr
            curr = curr.next
            to_traverse -= 1
        
        return head


        