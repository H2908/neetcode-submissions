# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):

        def height(node):
            if node is None:
                return 0

            return 1 + max(
                height(node.left),
                height(node.right)
            )

        if root is None:
            return 0

        diameter = height(root.left) + height(root.right)

        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)

        return max(diameter, left_diameter, right_diameter)