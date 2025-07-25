class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        for i in range(len(strs[0])):

            # Compare the character at index `i` with corresponding characters in all other strings
            for s in strs:
                #   1. Index `i` exceeds the length of current string (shorter string)
                #   2. Characters at index `i` don't match
                if i == len(s) or s[i] != strs[0][i]:
                    # Return the common prefix found so far using slicing up to index `i`
                    return strs[0][:i]

        # If loop completes without mismatches, entire first string is the common prefix
        return strs[0]

"""
📚 Concepts Used:
-----------------
- for loop: To iterate through indices and strings.
- if not strs: To handle empty list edge case.
- s[i] != strs[0][i]: To compare character at same index in all strings.
- strs[0][:i]: Slicing to return prefix up to a point of mismatch.
- List[str] and -> str: Python type hinting.

🎯 What We Learn:
-----------------
- How to find the longest common prefix among multiple strings.
- String indexing and slicing in Python.
- Handling edge cases like empty input.
- Efficient early termination when mismatch is found.
- Useful real-world string pattern problem seen in coding interviews.
"""
