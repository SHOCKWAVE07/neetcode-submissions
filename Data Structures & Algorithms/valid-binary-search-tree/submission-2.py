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


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans = []

        self.helper(root)

        for i in range(1,len(self.ans)):
            if self.ans[i-1]>=self.ans[i]:
                return False

        return True

        