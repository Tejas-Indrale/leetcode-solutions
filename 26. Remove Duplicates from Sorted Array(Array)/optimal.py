class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


'''📘 What We Learn (Key Concepts):
🔹 Problem:
Remove duplicates from a sorted array in-place and return the new length of the array without duplicates.

🔹 Pattern Used:
Two pointers (slow and fast) technique:

Slow pointer (i) keeps track of the position of unique elements.

Fast pointer (j) scans through the list to find new unique elements.

🔹 Time & Space:
Time Complexity: O(n) — we traverse the list only once.

Space Complexity: O(1) — no extra space used.'''