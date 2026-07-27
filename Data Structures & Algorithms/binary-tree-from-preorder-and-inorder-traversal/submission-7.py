# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_ind = {}
        for i, x in enumerate(inorder):
            inorder_ind[x] = i
        

        self.i = 0
        


        def helper(in_left, in_right):
            if in_left > in_right:
                return None


            root = TreeNode(preorder[self.i])
            mid = inorder_ind[preorder[self.i]]
            self.i += 1
            root.left = helper(in_left, mid-1)
            root.right = helper(mid+1, in_right)

            return root
        return helper(0, len(preorder) - 1)




