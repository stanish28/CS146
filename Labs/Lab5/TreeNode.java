package Lab5;

public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public boolean isValidBST(TreeNode root) {
    return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
}

private boolean isValidBST(TreeNode node, long lower, long upper) {
    if (node == null) return true;
    int val = node.val;
    if (val <= lower || val >= upper) return false;
    if (!isValidBST(node.right, val, upper)) return false;
    if (!isValidBST(node.left, lower, val)) return false;
    return true;
}
