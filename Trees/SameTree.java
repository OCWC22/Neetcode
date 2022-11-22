package Trees;
//LeetCode 100 Same Tree
//https://leetcode.com/problems/same-tree/description/

//https://www.youtube.com/watch?v=vRbbcKXCxOw

//DFS - Recursion preorder

class TreeNode{
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(){}
    TreeNode(int val){this.val = val;}
    TreeNode(int val, TreeNode left, TreeNode right){
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class SameTree {
    public boolean isSameTree(TreeNode p, TreeNode q){
        if (p == null && q == null) return true;
        if (p == null || q == null) return false;
        if (p.val != q.val) return false;
        return this.isSameTree(p.left, q.left) && this.isSameTree(p.right, q.right);
    }
    
}
