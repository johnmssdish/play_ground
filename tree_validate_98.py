class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Initialize variables for in-order traversal
        prev_val = float('-inf')

        # Helper function for in-order traversal
        def inorder_traversal(node):
            nonlocal prev_val

            if not node:
                return True

            # Traverse left subtree
            if not inorder_traversal(node.left):
                return False

            # Check current node's value
            if node.val <= prev_val:
                return False

            # Update prev_val with current node's value
            prev_val = node.val

            # Traverse right subtree
            return inorder_traversal(node.right)

        # Start the in-order traversal from the root
        return inorder_traversal(root)