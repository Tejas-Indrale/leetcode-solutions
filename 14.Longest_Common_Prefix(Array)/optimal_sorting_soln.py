from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If the list is empty, return an empty string
        if not strs:
            return ""

        # Step 1: Sort the strings
        strs.sort()

        # Step 2: Compare only the first and last strings
        first = strs[0]
        last = strs[-1]
        i = 0

        # Step 3: Find the common prefix between first and last strings
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1

        # Step 4: Return the common prefix found
        return first[:i]
