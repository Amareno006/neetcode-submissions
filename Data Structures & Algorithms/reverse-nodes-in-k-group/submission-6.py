# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = ListNode()
        current = res

  
        running_node = head

        while running_node:
            reverse = running_node
            prev = None
            for n in range(k-1):
                if running_node:
                    running_node = running_node.next
            if running_node: 
                next_group_start = running_node.next

                dummy = reverse
                for n in range(k): 
                    forward = reverse.next
                    reverse.next = prev 
                    prev = reverse
                    reverse = forward
                current.next = prev
                current = dummy
                running_node = next_group_start

            else: 
                current.next = reverse
        return res.next

                
            

            
            
