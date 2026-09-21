# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p and q:
            return False
        
        if not q and p:
            return False


        if p.val != q.val:
            return False

        if p.left and q.left:
            left = self.isSameTree(p.left,q.left)
        elif p.left or q.left:
            left = False
        else:
            left = True

        if p.right and q.right:
            right = self.isSameTree(p.right,q.right) 
        elif p.right or q.right:
            right = False
        else:
            right = True

        return left and right

            


            
        