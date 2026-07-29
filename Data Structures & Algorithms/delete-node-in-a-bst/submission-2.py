# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        cur = root
        prev = root
        while cur:
            if key == cur.val:
                break
            prev = cur
            if key < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        if not cur:
            return root

        left = cur.left
        right = cur.right

        if cur == root:
            if root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                return None

        if cur.val < prev.val:
            if left:
                prev.left = left
            else:
                prev.left = right
                return root
        else:
            if left:
                prev.right = left
            else:
                prev.right = right
                return root

        ref = left
        while ref.right:
            ref = ref.right

        ref.right = right

        return root