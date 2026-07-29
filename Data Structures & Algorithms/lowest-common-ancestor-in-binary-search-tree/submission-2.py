# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = root

        if p.val > q.val:
            p, q = q, p

        while res:
            if p.val <= res.val <= q.val:
                return res
            if res.val < p.val:
                res = res.right
            else:
                res = res.left

        return res