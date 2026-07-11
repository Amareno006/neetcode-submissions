# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = ListNode()
        current = res

  

        while head:
            reverse = head
            prev = None
            for n in range(k-1):
                if head:
                    head = head.next
            if head: 
                next_group_start = head.next

                dummy = reverse
                for n in range(k): 
                    forward = reverse.next
                    reverse.next = prev 
                    prev = reverse
                    reverse = forward
                current.next = prev
                current = dummy
                head = next_group_start

            else: 
                current.next = reverse
        return res.next

                
            

            
            
