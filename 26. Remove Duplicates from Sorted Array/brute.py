class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0  
        while i < len(nums) - 1:  
            if nums[i] == nums[i + 1]:  # If current element is same as next (duplicate)
                nums.pop(i + 1)  # Remove the duplicate element
                # Don't move 'i' forward because the list shifts left after pop
            else:
                i += 1  # Move to next element if no duplicate
        return len(nums)  
    

"""🔹 Use while when you need to modify a list (like deleting elements) and control loop flow precisely.
🔹 Avoid for when list size changes during iteration — it’s not safe."""
