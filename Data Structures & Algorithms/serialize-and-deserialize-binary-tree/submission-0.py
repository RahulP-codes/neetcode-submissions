# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = []

        dq = deque([root])
        while dq:
            node = dq.popleft()

            if not node:
                res.append("#")
                continue
            
            res.append(str(node.val))

            dq.append(node.left)
            dq.append(node.right)

        return "-".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        arr = data.split("-")

        root = TreeNode(int(arr[0]))
        dq = deque([root])

        idx = 1
        while idx < len(arr) and dq:
            node = dq.popleft()
            if not node:
                continue

            node.left = TreeNode(int(arr[idx])) if arr[idx] != '#' else None
            dq.append(node.left)
            idx += 1

            node.right = TreeNode(int(arr[idx])) if arr[idx] != '#' else None
            dq.append(node.right)
            idx += 1

        return root



