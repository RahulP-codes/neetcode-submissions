# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = root.val

        def dfs(node):
            nonlocal maxSum

            if not node:
                return 0

            lmax = dfs(node.left)
            rmax = dfs(node.right)

            lmax = max(0, lmax)
            rmax = max(0, rmax)
            
            maxSum = max(maxSum, lmax + rmax + node.val)

            return max(lmax, rmax) + node.val

        dfs(root)

        return maxSum
        