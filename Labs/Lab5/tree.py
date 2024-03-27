class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root, lower, upper):
    if not root:
        return True
    val = root.val
    if val <= lower or val >= upper:
        return False
    if not isValidBST(root.right, val, upper):
        return False
    if not isValidBST(root.left, lower, val):
        return False
    return True
