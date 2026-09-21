# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self,root,prev):
        
        if not root:
            return

        if root.val >= prev:
            self.index+=1
            prev = root.val

        self.helper(root.left,prev)
        self.helper(root.right,prev)

        return

    def goodNodes(self, root: TreeNode) -> int:

        self.index = 0
        prev = root.val

        self.helper(root,prev)

        return self.index




        