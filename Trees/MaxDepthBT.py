 #Leetcode 104
 #https://leetcode.com/problems/maximum-depth-of-binary-tree/

 #https://www.youtube.com/watch?v=hTM3phVI6YQ&t=4s

 # Recursive DFS
 # O(n) time
 
"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

            3
          /   \
         9     20
              /  \
            15    7

Example 2:
Input: root = [1,null,2]
Output: 2

            1
              \   
                2
"""
    
from collections import deque 

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
#Recursion DFS
class Solution:
    def maxDepth(self, root: TreeNode):
        if not root:
            return 0
        else:
            leftV = self.maxDepth(root.left)
            rightV = self.maxDepth(root.right)
            return max(leftV, rightV) + 1

#BFS solution
class Solution:
    def maxDepth(self, root: TreeNode):
        if not root:
            return 0
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level   

#Preorder Iterative DFS (root -> left -> right)
class Solution:
    def maxDepth(self, root: TreeNode):
 
        #stack stores the root (Node) and the levels 
        stack = [[root, 1]]
        result = 0
        
        while stack:
            node, depth = stack.pop()

            #conditional to ignore null nodes if present
            if node:
                result = max(result, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return result
                 