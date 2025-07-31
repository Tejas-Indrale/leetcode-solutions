from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildBST(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            node.left = buildBST(left, mid - 1)
            node.right = buildBST(mid + 1, right)
            return node

        return buildBST(0, len(nums) - 1)


        """
        Technique Used:
        - Optimal divide-and-conquer approach using index boundaries instead of array slices.
        - Avoids memory overhead from slicing by reusing the original array.
        - Recursively picks the middle element as root to ensure balance.
        - Time Complexity: O(n)
        - Space Complexity: O(log n) for recursion stack (balanced tree has log n depth).



| Approach    | Time Complexity | Space Complexity | Extra Memory Used | Balanced? |
| ----------- | --------------- | ---------------- | ----------------- | --------- |
| Brute-force | O(n)            | O(n)             | Yes (slicing)     | ✅ Yes     |
| **Optimal** | O(n)            | O(log n)         | ❌ No slicing      | ✅ Yes     |

        """
