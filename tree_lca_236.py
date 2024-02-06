class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        if root is None or root == p or root == q:
            return root

        # Recursively search in the left and right subtrees.
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right subtrees have an LCA, then the current root is the LCA.
        if left_lca and right_lca:
            return root

        # If either left or right subtree has an LCA, return that LCA.
        return left_lca if left_lca else right_lca