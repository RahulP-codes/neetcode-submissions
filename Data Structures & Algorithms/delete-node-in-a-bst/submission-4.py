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
        parent = root
        while cur:
            if key == cur.val:
                break
            parent = cur
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

        if cur.val < parent.val:
            if left:
                parent.left = left
            else:
                parent.left = right
                return root
        else:
            if left:
                parent.right = left
            else:
                parent.right = right
                return root

        ref = left
        while ref.right:
            ref = ref.right

        ref.right = right

        return root