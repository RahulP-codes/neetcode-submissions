# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        if not preorder:
            return None

        # print("=============")
        # print(f"pre: {preorder}")
        # print(f"in: {inorder}")

        idx = 0
        jdx = 0
        done = False
        for i in range(len(preorder)):
            if done:
                break
            for j in range(len(inorder)):
                if preorder[i] == inorder[j]:
                    idx = i
                    jdx = j
                    done = True
                    break
            

        # print(f"idx, jdx = {idx}, {jdx}")

        left = self.buildTree(preorder[idx+1:], inorder[:jdx])
        right = self.buildTree(preorder[idx+1:], inorder[jdx+1:])
        
        # print(f"pre[idx]: {preorder[idx]}")
        return TreeNode(preorder[idx], left, right)