# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        x = 0 
        y = 0 
        l1_val = 0
        l2_val = 0
        while l1 or l2:
            if l1:  
                l1_val += l1.val * (10 ** x)
                x += 1
                l1 = l1.next
            if l2: 
                l2_val += l2.val * (10 ** y)
                y += 1
                l2 = l2.next
        
        val = l1_val + l2_val
        res = ListNode(val % 10)

        val -= (val% 10)
        copy = res
        z = 1
        while val != 0: 
            digit = val % (10 ** (z+1))
            val -= digit

            res.next = ListNode(int(digit / (10 ** z)))
            res = res.next
            z += 1

        res.next = None

        return copy
        