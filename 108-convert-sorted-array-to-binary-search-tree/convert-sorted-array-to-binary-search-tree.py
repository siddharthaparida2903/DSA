# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        root = TreeNode(0)
        stack = [(root, 0, len(nums) - 1)]

        while stack:
            node, l, r = stack.pop()
            m = (l + r) // 2
            node.val = nums[m]
            if l <= m - 1:
                node.left = TreeNode(0)
                stack.append((node.left, l, m - 1))
            if m + 1 <= r:
                node.right = TreeNode(0)
                stack.append((node.right, m + 1, r))

        return root