from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Initialize pointers:
        i = m - 1        # Pointer for the last valid element in nums1
        j = n - 1        # Pointer for the last element in nums2
        k = m + n - 1    # Pointer for the last position in nums1 (including extra space)

        # Merge from the back to avoid overwriting values in nums1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If any elements are left in nums2, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        # Technique Used:
        # This is an optimal in-place merging approach using three pointers:
        # - 'i' for the last valid element in nums1,
        # - 'j' for the last element in nums2,
        # - 'k' for the position to insert the next largest value in nums1.
        # It starts filling nums1 from the end to prevent overwriting valid data.
        # First, it compares elements from the end and places the larger one at nums1[k].
        # Then, if any elements are left in nums2, they are copied to nums1.
        # Time Complexity: O(m + n), Space Complexity: O(1), all done in-place.
