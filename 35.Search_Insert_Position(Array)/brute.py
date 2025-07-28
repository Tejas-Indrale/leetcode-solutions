class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        
        return len(nums)




    # O(n) time complexity:
    # not an optimal solution, cause it  checks each element in the array , takes time
    # for sorted array use binary search insted O(log n) time complexity