# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def matching(self,root,subroot):

        if not root and not subroot:
            return True

        elif (root and subroot) and (root.val == subroot.val):
            left = self.matching(root.left,subroot.left)
            right = self.matching(root.right,subroot.right)
            return left and right
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True

        if not root:
            return False

        if self.matching(root,subRoot):
            return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

