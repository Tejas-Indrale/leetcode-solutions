from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Start from the end of both arrays
        i = m - 1  # Last element in nums1's actual data
        j = n - 1  # Last element in nums2

        # Iterate backwards from the end of nums1
        for k in range(m + n - 1, -1, -1):
            if i < 0:
                nums1[k] = nums2[j]
                j -= 1

            elif j < 0:
                break

            elif nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1

            else:
                nums1[k] = nums2[j]
                j -= 1

        # Technique Used:
        # This approach uses a reverse traversal with a single for-loop.
        # We maintain three pointers: 
        # - 'i' points to the last valid element in nums1,
        # - 'j' points to the last element in nums2,
        # - 'k' is the index where the current largest element should be placed in nums1.
        # By comparing elements from the back and filling nums1 from the end,
        # we ensure no useful data is overwritten.
        # This method is optimal with Time Complexity: O(m + n), Space Complexity: O(1), and is done in-place.
