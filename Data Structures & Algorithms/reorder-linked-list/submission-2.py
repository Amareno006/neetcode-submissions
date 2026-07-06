# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        prev = None
        secondHead = head

        original = head


        while secondHead.next and secondHead.next.next: 
            secondHead = secondHead.next.next
            head = head.next

        replica = head.next
        head.next = None

        while replica: 
            temp = replica.next
            replica.next = prev
            prev = replica
            replica = temp

        p1 = original 
        p2 = prev

        while p2: 
            p1_next = p1.next
            p1.next = p2
            p2_next = p2.next
            p2.next = p1_next
            p1 = p1_next
            p2 = p2_next

        return None