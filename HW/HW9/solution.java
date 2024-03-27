package HW.HW9;

   
public class solution extends problem{
    public problem lowestCommonAncestor(problem root, problem p, problem q) {
        if (root == null) return null;
        
        if (p.val > root.val && q.val > root.val) {
            // Both nodes are in the right subtree
            return lowestCommonAncestor(root.right, p, q);
        } else if (p.val < root.val && q.val < root.val) {
            // Both nodes are in the left subtree
            return lowestCommonAncestor(root.left, p, q);
        } else {
            // We have found the split point, i.e., the LCA node
            return root;
        }
    }
}