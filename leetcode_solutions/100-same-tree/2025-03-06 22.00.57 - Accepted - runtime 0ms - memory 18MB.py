# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 如果兩個節點都為 None，表示結構相同
        if not p and not q:
            return True
        # 如果其中一個節點為 None 或者值不同，則回傳 False
        if not p or not q or p.val != q.val:
            return False
        # 遞迴檢查左子樹與右子樹是否相同
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
