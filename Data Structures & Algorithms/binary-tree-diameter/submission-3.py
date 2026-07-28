# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node, count):
            nonlocal res

            if not node:
                return count-1

            ld = dfs(node.left, count+1)
            rd = dfs(node.right, count+1)
            maxd = max(ld, rd)

            res = max(res, ld-count+rd-count)

            return maxd

        dfs(root, 0)

        return res

            