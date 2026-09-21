# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper(self,preorder,inorder):
        if not preorder or not inorder:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)

        pivot = inorder.index(root_val)


        left_size = pivot 

        root.left = self.helper(preorder[1:1+left_size],inorder[:pivot])
        root.right = self.helper(preorder[1+left_size:],inorder[pivot+1:])

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        self.mp = dict()

        for i in range(len(inorder)):
            self.mp[inorder[i]] = i

        return self.helper(preorder,inorder)
        