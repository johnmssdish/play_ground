import copy
a=[1,2,3]
b=[5,6,7]
d=copy.deepcopy(b)
b.append(111)
print(d)
print(a+b)

for i in range(3):
    print('oo')
    if i ==1:
        break
print('po')

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

