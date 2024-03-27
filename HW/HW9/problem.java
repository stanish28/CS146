package HW.HW9;

public class problem {
        int val;
        problem left;
        problem right;
        problem() {}
        problem(int val) { this.val = val; }
        problem(int val, problem left, problem right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
}

   
class solution {
    public problem lowestCommonAncestor(problem root, problem p, problem q) {
        if (root == null) return null;
        
        if (p.val > root.val && q.val > root.val) {
            return lowestCommonAncestor(root.right, p, q);
        } else if (p.val < root.val && q.val < root.val) {
            return lowestCommonAncestor(root.left, p, q);
        } else {
            return root;
        }
    }
}
 
    