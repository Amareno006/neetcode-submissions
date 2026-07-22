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
        i = 0
        while (i != len(nodes)): 
            vals = []
            z = len(nodes) - i
            for x in range(z): 
                vals.append(nodes[i].val)
                if nodes[i].left:
                    nodes.append(nodes[i].left)
                if nodes[i].right: 
                    nodes.append(nodes[i].right)
                i += 1
            res.append(vals)


        return res

        




            