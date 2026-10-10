# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []

        def traverse(node, i):
            if node is None:
                return
            if i < len(levels):
                levels[i].append(node.val)
            else:
                levels.append([node.val])
            
            if node.left:
                traverse(node.left, i + 1)
            if node.right:
                traverse(node.right, i + 1)

        traverse(root, 0)
        return levels