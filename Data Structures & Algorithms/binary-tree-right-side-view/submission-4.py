# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        i = 0 
        if not root:
            return []
        res = []
        nodes = [root]


        while (i != (len(nodes))):
            res.append(nodes[-1].val) 

            ind = len(nodes) - i

            for x in range(ind): 
                if nodes[i].left:
                    nodes.append(nodes[i].left)
                if nodes[i].right: 
                    nodes.append(nodes[i].right)
                i += 1

        return res