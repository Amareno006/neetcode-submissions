# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        nodes_p = [p]

        nodes_q = [q]

        if bool(p) != bool(q): 
            return False

        if p == None and q == None: 
            return True

        while nodes_p and nodes_q:

            curr_p = nodes_p.pop(0)
            curr_q = nodes_q.pop(0)
            if curr_p.val != curr_q.val: 
                return False
            if bool(curr_p.left) == bool(curr_q.left): 
                if curr_p.left: 
                    nodes_p.append(curr_p.left)
                    nodes_q.append(curr_q.left)
            else: 
                return False

            if bool(curr_p.right) == bool(curr_q.right): 
                if curr_p.right: 
                    nodes_p.append(curr_p.right)
                    nodes_q.append(curr_q.right)
            else: 
                return False
        return True
