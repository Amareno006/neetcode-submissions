# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.isTrue = True


        def dfs(node): 
            if not self.isTrue: 
                return 0, 0
            if not node: 
                return float('inf'), float('-inf')

        
            left_min, left_max = dfs(node.left)

            right_min, right_max = dfs(node.right)
            if left_max >= node.val: 
                self.isTrue = False
            if right_min <= node.val: 
                self.isTrue = False
            return min([node.val, left_min, right_min]), max([node.val, right_max, left_max])
        dfs(root)
        return self.isTrue
                
