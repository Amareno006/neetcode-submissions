# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        curr_node = [root]
        res = ""
        while curr_node: 
            node = curr_node.pop()

            if node:
                res += f"{node.val},"
                curr_node.append(node.right)
                curr_node.append(node.left)


            else: 
                res += "N,"

        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        lett = data.split(',')
        self.i = 0
        def dfs(): 
            if lett[self.i] == "N": 
                self.i += 1
                return None

            node = TreeNode(int(lett[self.i]))
            self.i += 1
            left_node = dfs()
            right_node = dfs()

            node.left = left_node
            node.right = right_node
            return node
        return dfs()
