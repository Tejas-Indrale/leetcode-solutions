class Solution(object):
    def twoSum(self, nums, target):
        # Create an empty hashmap (dictionary) to store number as key and its index as value
        hashmap = {}

        for i in range(len(nums)):
            # Find the complement that, when added to nums[i], gives the target
            complement = target - nums[i]

            # If the complement is already in hashmap, solution found
            if complement in hashmap:
                # Return the indices: index of complement and current index
                return [hashmap[complement], i]

            # If not found, store the current number and its index in hashmap
            else:
                hashmap[nums[i]] = i

        # Return empty list if no pair found (though problem guarantees one solution)
        return []

"""
📘 Hashmap Explanation:
- A hashmap (dictionary) allows fast O(1) lookup using keys.
- We use it to store previously seen numbers and their indices.
- For each element, we ask: "Have we already seen the number that adds up to the target?"
- If yes → return both indices.
- If no → save this number in the hashmap for later use.

📘 Code Concepts:
- self → Refers to the instance of the class.
- range(len(nums)) → Generates list indices for iteration.
- hashmap[key] = value → Stores number:index mapping.
- if key in hashmap → Checks for existence in O(1) time.

⏱️ Time Complexity: O(n)
📦 Space Complexity: O(n)
"""
