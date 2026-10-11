# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        @cache
        def size(node):
            if node is None:
                return 0

            l = size(node.left)
            r = size(node.right)

            return 1 + l + r

        def find_kth(node, num_to_left):
            if node is None:
                return 0

            l = size(node.left)
            current_place = num_to_left + l + 1

            if current_place == k:
                return node.val

            if current_place > k:
                return find_kth(node.left, num_to_left)

            return find_kth(node.right, current_place)

        return find_kth(root, 0)