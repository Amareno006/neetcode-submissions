# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.best = float('-inf')
        def dfs(node): 
            if not node: 
                return 0 
            

            left_max = dfs(node.left)
            right_max = dfs(node.right)
            self.best = max(self.best, node.val, node.val + left_max, node.val + right_max, node.val + left_max + right_max )
            return max(node.val, node.val + left_max, node.val + right_max)
        dfs(root)
        return self.best

