# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new = TreeNode(val)
        if not root:
            return new

        cur = root
        prev = root
        while cur:
            prev = cur
            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
                
        if val < prev.val:
            prev.left = new
        else:
            prev.right = new

        return root