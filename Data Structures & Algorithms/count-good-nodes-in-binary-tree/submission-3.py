# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root: 
            res = 1
            node = [root]
            best = [root.val]
        else: 
            return 0

        

        while node:
            i = len(node)

            for x in range(i):
                if node[0].left: 
                    node.append(node[0].left)
                    if node[0].left.val >= best[0]: 
                        best.append(node[0].left.val)
                        res += 1
                    else: 
                        best.append(best[0])

                if node[0].right: 
                    node.append(node[0].right)
                    if node[0].right.val >= best[0]: 
                        best.append(node[0].right.val)
                        res += 1
                    else: 
                        best.append(best[0])
            
                node.pop(0)
                best.pop(0)
        return res

            