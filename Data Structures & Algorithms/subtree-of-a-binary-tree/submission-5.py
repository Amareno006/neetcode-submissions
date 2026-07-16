# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not subRoot: 
                return True
            if not root: 
                return False
                
            def isSameTree(p, q):
                stack = [(p, q)]

                while stack: 
                    node_p, node_q = stack.pop(0)
                    if not node_p and not node_q: 
                        continue
                        
                    if not node_p or not node_q or node_p.val != node_q.val: 
                        return False

                    stack.append((node_p.left, node_q.left))
                    stack.append((node_p.right, node_q.right))

                return True

            def bfs(node): 
                seen_nodes = [node]

                while seen_nodes: 
                    res = False
                    curr_node = seen_nodes.pop()
                    if curr_node.val == subRoot.val:
                        res = isSameTree(curr_node, subRoot)

                    if res: 
                        return True
                    if curr_node.left: 
                        seen_nodes.append(curr_node.left)
                    if curr_node.right: 
                        seen_nodes.append(curr_node.right)
                return False

            return bfs(root)

                    
                    