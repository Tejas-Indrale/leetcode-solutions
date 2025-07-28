class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            m = (l+r) // 2

            if nums[m] > target:
                r = m -1
            elif nums[m] < target:
                l = m + 1
            else :
                return m
            

        # If target not found:
        # - If it's greater than nums[m], insert after m → m + 1
        # - If it's less, insert at m

        if nums[m] < target:
            return m + 1
        else :
            return m


        
# Binary Search works on sorted arrays by repeatedly dividing the search range in half.
        # At each step, we compare the target with the middle element:
        # - If target == middle → we found it.
        # - If target < middle → search in the left half.
        # - If target > middle → search in the right half.
        # This helps reduce time complexity to O(log n).






      




        