# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 基礎情況：如果節點為空，回傳 0
        if not root:
            return 0
        
        # 計算左右子樹的深度
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # 回傳最大深度 + 1（包含當前節點）
        return max(left_depth, right_depth) + 1
        