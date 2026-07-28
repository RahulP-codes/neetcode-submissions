# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = True

        def dfs(node1, node2):
            nonlocal res
            if not res:
                return

            print(bool(node1), bool(node2))

            if not node1 and not node2:
                return

            if node1 or node2:
                if not (node1 and node2):
                    print("1")
                    res = False
                    return

            if node1.val != node2.val:
                print("2")
                res = False
                return

            dfs(node1.left, node2.left)
            dfs(node1.right, node2.right)

        dfs(p, q)

        return res

            

            