# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        full_list = []
        for n in lists: 
            while n: 
                full_list.append(n.val)
                n = n.next
        
        full_list.sort()

        new_link = ListNode(0)
        res = new_link

        for x in full_list: 
            new_link.next = ListNode(x)
            new_link = new_link.next
        return res.next
        