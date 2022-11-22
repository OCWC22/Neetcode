package Trees;
//https://leetcode.com/problems/invert-binary-tree/description/

class TreeNode{
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(){}

    TreeNode(int val){
        this.val = val;
    }
    TreeNode(int val, TreeNode left, TreeNode right){
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution{
    public TreeNode invertTree(TreeNode root){
        if (root == null)
            return null;
        TreeNode left = this.invertTree(root.left);
        TreeNode right = this.invertTree(root.right);
        root.left = right;
        root.right = left;
        return root;
    }
}