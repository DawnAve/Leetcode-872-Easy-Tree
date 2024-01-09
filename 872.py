# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        # Two arrays for the leaves
        A = []
        B = []
        def dfs(root,ans):

            # Check if it is a leave
            if root.left == None and root.right == None:
                ans.append(root.val)

                # DFS
            else:
                if root.left:
                    dfs(root.left, ans)
                if root.right:
                    dfs(root.right, ans)
        dfs(root1, A)
        dfs(root2, B)
        return A == B
            
