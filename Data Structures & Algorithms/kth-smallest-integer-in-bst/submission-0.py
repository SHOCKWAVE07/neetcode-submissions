# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper(self,root):

        if not root:
            return

        self.helper(root.left)
        self.ans.append(root.val)
        self.helper(root.right)

        return 

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = []

        self.helper(root)
     
        return self.ans[k-1]

        
        