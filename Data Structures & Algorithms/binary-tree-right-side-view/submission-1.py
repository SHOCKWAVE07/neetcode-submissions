# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper(self,root,level):

        if not root:
            return

        self.helper(root.left,level+1)
        self.helper(root.right,level+1)

        self.ans[level] = root.val

        return 



    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = dict()
        level = 0
        self.helper(root,level)
        result = []
        print(self.ans)
        for i in range(len(self.ans)):
            result.append(self.ans[i])
        return result


        