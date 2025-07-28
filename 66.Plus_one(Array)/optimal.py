class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # Loop from the last digit to the first
        for i in range(n - 1, -1, -1):  # i goes from n-1 to 0
            if digits[i] < 9:
                digits[i] += 1       # Just add 1 if digit is less than 9
                return digits        # No carry needed, return result
            digits[i] = 0            # If digit is 9, set to 0 and continue (carry over)

        # If loop finishes, it means all digits were 9 (e.g., [9,9,9])
        return [1] + digits         # Add 1 at the beginning, e.g., [1,0,0,0]
