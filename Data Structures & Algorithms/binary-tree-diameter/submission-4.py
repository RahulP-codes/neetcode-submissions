# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res

            if not node:
                return 0

            ld = dfs(node.left)
            rd = dfs(node.right)
            maxd = max(ld, rd)

            res = max(res, ld+rd)

            return 1 + maxd

        dfs(root)

        return res

            