# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        

        def dfs(node):
            if not node:
                return (0, 0)

            lmax0, lmax1 = dfs(node.left)
            rmax0, rmax1 = dfs(node.right)

            curmax0 = max(lmax0, lmax1) + max(rmax0, rmax1)
            curmax1 = lmax0 + rmax0 + node.val
            print(f"val: {node.val}, max: ({curmax0}, {curmax1})")
            print("left", lmax0, lmax1)
            print("right", rmax0, rmax1)

            return (curmax0, curmax1)

        a = dfs(root)
        print(a)
        return max(dfs(root))