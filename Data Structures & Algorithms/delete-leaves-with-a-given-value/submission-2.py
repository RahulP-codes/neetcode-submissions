# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)

            if node.left and node.left.val == 0:
                node.left = None
            if node.right and node.right.val == 0:
                node.right = None
            
            if node.val == target and not node.left and not node.right:
                node.val = 0

            
        dfs(root)

        if root.val == 0:
            return None

        return root

            

        