# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSame(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not (p and q):
            return False
        if p.val != q.val:
            return False

        return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        find = subRoot.val
        res = False

        q1 = deque([root])
        while q1:
            node = q1.popleft()
            
            if not node:
                continue

            if node.val == find:
                res = self.isSame(node, subRoot)
                if res:
                    return res
            
            q1.append(node.left)
            q1.append(node.right)

        return res