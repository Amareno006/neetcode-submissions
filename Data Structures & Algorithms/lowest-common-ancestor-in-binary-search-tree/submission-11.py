# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        parents = {}

        parents[root] = root

        curr_node = [root]


        while curr_node: 
            node = curr_node.pop(0)

            if node: 
                if node.left: 
                    parents[node.left] = node
                    curr_node.append(node.left)

                if node.right: 
                    parents[node.right] = node
                    curr_node.append(node.right)

        for node in parents:
            if node.val == p.val:
                p = node
            if node.val == q.val:
                q = node
        ancestors = set()
        while p: 
            ancestors.add(p)
            if p == root: 
                break
            p = parents[p]
        while True: 
            if q in ancestors: 
                return q
            q = parents[q]

            