# Brute-force solution to the Two Sum problem
# Time Complexity: O(n^2)
# Idea: Check every possible pair of numbers to see if their sum equals the target.

class Solution:
    # The "self" parameter represents the current object of the class.
    # Whenever we call: Solution().twoSum(nums, target)
    # Python internally does: Solution.twoSum(object, nums, target)
    def twoSum(self, nums, target):
        # range(len(nums)) → range() generates numbers from 0 to len(nums)-1.
        # Example: if nums = [2,7,11,15], len(nums) = 4 → range(4) = [0,1,2,3]
        for i in range(len(nums)):
            # Start the second loop from i+1 so we don't use the same element twice
            # Example: i=0 → j runs from 1 to 3 (indexes after i)
            for j in range(i + 1, len(nums)):
                
                # If nums[i] + nums[j] equals target, we found the answer
                if nums[i] + nums[j] == target:
                    # Return the two indices [i, j]
                    return [i, j]

        # This return is only reached if no pair is found.
        return []

# ------------------------ LESSONS LEARNED ------------------------
# 1. self: Used as the first parameter in class methods to refer to the object itself.
# 2. range(): A built-in Python function that generates a sequence of numbers.
#    Example: range(5) → [0,1,2,3,4]
# 3. len(): Gives the length (number of elements) in a list.
# 4. for loop: Used to iterate over a sequence (e.g., range of numbers).
# 5. return: Immediately exits the function and gives a result.
# 6. Class & Object: We define "Solution" as a class and create an object (sol = Solution()) to call its function.

# Example usage
nums = [2, 7, 11, 15]   # Input list
target = 9              # Target sum we need to find
sol = Solution()        # Create an object of Solution class
print(sol.twoSum(nums, target))  # Output: [0, 1] because 2 + 7 = 9
