# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = [[]]
        dq = deque([root])

        idx = 0
        lev = 1
        while dq:
            node = dq.popleft()

            if lev == idx:
                res.append([])
                lev += len(dq)+1

            res[-1].append(node.val)

            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)

            idx += 1

        return res