# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        dummy = ListNode(0)

        dummy.next = head
        x = 0
        while head: 
            head = head.next
            x += 1
        length = x - n

        print(length)

        copy = dummy
        for z in range(length): 
             copy = copy.next
        
        if copy.next and copy.next.next:
            copy.next = copy.next.next
        else: 
            copy.next = None



        return dummy.next
