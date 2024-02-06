# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque([root])
        node_list=[]
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                node_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        node_list.sort()
        return node_list[k-1]
    





        # others:
        count = 0
        result = None

        # Helper function for in-order traversal
        def inorder_traversal(node):
            nonlocal count, result

            if not node:
                return

            # Traverse left subtree
            inorder_traversal(node.left)

            # Increment count when visiting a node
            count += 1

            # If count reaches k, update result and stop traversal
            if count == k:
                result = node.val
                return

            # Traverse right subtree
            inorder_traversal(node.right)

        # Start the in-order traversal from the root
        inorder_traversal(root)

        return result