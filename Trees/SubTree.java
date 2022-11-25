package Trees;
//Leetcode 527
//https://leetcode.com/problems/subtree-of-another-tree/description/

//https://www.youtube.com/watch?v=E36O5SWp-LE
//https://neetcode.io/practice


class Solution {
   public boolean isSubtree(TreeNode root, TreeNode subRoot) {
       if (root == null && subRoot == null)
           return true;
       if (root == null || subRoot == null)
           return false;
       if (sameTree(root, subRoot))
           return true; 
       return (isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot));
       
   }

   private boolean sameTree(TreeNode root, TreeNode subRoot){
       if (root == null && subRoot == null)
           return true;
       if (root == null || subRoot == null)
           return false;
       if (root.val == subRoot.val){
           return (sameTree(root.left, subRoot.left) && sameTree(root.right, subRoot.right));
       }
       return false;
   }

}