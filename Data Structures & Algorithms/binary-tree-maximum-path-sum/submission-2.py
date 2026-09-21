# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper(self,root):
        if not root:
            return 0

        curr = root.val

        left = self.helper(root.left)
        right = self.helper(root.right)

        temp = curr+left+right

        self.maxi = max(self.maxi,temp)

        return max(max(curr,max(left,right)+curr),0)




    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.maxi = root.val

        self.helper(root)

        return self.maxi