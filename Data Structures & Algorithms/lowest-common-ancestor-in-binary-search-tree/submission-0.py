# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def common_node(self,root,p,q):

        if not root:
            return False

        mid = (root.val == p.val or root.val == q.val)

        left = self.common_node(root.left,p,q)
        right = self.common_node(root.right,p,q)


        if mid + left + right > 1:
            self.common = root

        return left or right or mid


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.common = None
        self.common_node(root,p,q)

        return self.common
        