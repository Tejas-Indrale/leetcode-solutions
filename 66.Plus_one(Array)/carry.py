class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1  # Initially, we want to add 1 to the number (so carry is 1)
        i = 0

        digits = digits[::-1]  # Reverse the list to make it easier to start from the least significant digit

        while carry:
            if i < len(digits):  # If we are still within the bounds of the digits list
                if digits[i] == 9:
                    digits[i] = 0  # 9 becomes 0 and carry remains 1
                else:
                    digits[i] += 1  # Just add 1 and we're done
                    carry = 0  # No more carry needed
            else:
                digits.append(1)  # If all digits were 9 and we are out of bounds, add a new 1
                carry = 0  # No more carry needed

            i += 1  # Move to the next digit (to the left in original number)

        return digits[::-1]  # Reverse back the list to original order before returning


# --- How this code works ---
# This code adds 1 to a number represented by a list of digits.
# It handles carry manually, by reversing the list to go from least to most significant digit.
# If a digit is 9, it becomes 0 and carry continues.
# If it's less than 9, we simply add 1 and stop carrying.
# If we reach beyond the most significant digit, we just append 1.
# At the end, we reverse the list again to restore the correct order.
