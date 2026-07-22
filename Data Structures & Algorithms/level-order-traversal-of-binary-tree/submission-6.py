# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: 
            return []
        nodes = [root]
        res = []
        while nodes: 
            vals = []
            z = len(nodes)
            for x in range(z): 
                vals.append(nodes[0].val)
                if nodes[0].left:
                    nodes.append(nodes[0].left)
                if nodes[0].right: 
                    nodes.append(nodes[0].right)
                nodes.pop(0)
            res.append(vals)


        return res

        




            