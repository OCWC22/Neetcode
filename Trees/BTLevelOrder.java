package Trees;
//Leetcode 102
//Binary Tree Level Order Traversal
//https://leetcode.com/problems/binary-tree-level-order-traversal/solutions/
//https://neetcode.io/practice
import java.util.*;


class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(){}
    TreeNode(int val) {
        this.val = val;
    }
    TreeNode(int val, TreeNode left, TreeNode right){
        this.val = val;
        this.left = left;
        this.right = right;
    }
    
}

class Solution{
    public List<List<Integer>> levelOrder(TreeNode root){
        List<List<Integer>> res = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();

        if (root == null) 
            return res;

        q.add(root);
        while(!q.isEmpty()){
            int len = q.size();
            List<Integer> level = new ArrayList<>();
            for (int i = 0; i < len; i++){
                TreeNode curr = q.poll();
                
                level.add(curr.val);

                if (curr.left != null){                    
                    q.add(curr.left);
                }
                if (curr.right != null){
                    q.add(curr.right);
                }
            }
            res.add(level);
        }
        return res;
    }
}