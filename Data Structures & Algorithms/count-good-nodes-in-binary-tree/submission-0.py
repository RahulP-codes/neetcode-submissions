# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        prevMax = -100
        def backtrack(node, prevMax):
            nonlocal count

            if node.val >= prevMax:
                prevMax = node.val
                count += 1
            if node.right:
                backtrack(node.right, prevMax)
            if node.left:
                backtrack(node.left, prevMax)

        backtrack(root, prevMax)

        return count