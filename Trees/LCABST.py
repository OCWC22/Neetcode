#Leetcode 235
#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
#https://www.youtube.com/watch?v=gs2LMfuOR9k


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right =None

class Solution:
    def lowestCommonAncestor(self, root, p, q) -> 'TreeNode':
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur