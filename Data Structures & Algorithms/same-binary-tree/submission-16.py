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

        if not p: 
            return True

        while nodes_p and nodes_q:

            node = (nodes_p.pop(0), nodes_q.pop(0))
            if node[0].val != node[1].val: 
                return False
            if bool(node[0].left) == bool(node[1].left): 
                if node[0].left: 
                    nodes_p.append(node[0].left)
                    nodes_q.append(node[1].left)
            else: 
                return False

            if bool(node[0].right) == bool(node[1].right): 
                if node[1].right: 
                    nodes_p.append(node[0].right)
                    nodes_q.append(node[1].right)
            else: 
                return False
        return True
