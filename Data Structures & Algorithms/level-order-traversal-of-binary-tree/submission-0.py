# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper(self, root, level):

        if not root:
            return

        if level not in self.ans:
            self.ans[level] = [root.val]
        else:
            self.ans[level].append(root.val)

        self.helper(root.left,level+1)
        self.helper(root.right,level+1)

        return

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        self.ans = dict()
        level = 0
        self.helper(root,level)

        results = []

        for i in self.ans.keys():
            results.append(self.ans[i])

        return results