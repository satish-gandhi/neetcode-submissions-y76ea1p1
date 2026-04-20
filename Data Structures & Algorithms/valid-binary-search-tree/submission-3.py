# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.bstcheck(-inf, root, inf)
    def bstcheck(self, l, root, h):
        if not root:
            return True
        if not l<root.val<h:
            return False
        return self.bstcheck(l, root.left, root.val) and self.bstcheck(root.val, root.right, h)

        