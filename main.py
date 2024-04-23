# 7. Reverse Integer
# Solved
# Medium
# Topics
# Companies
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1

########################################################################################################################
class Solution(object):
    def reverse(self, x):
        if x<10 and x>=0: return x
        s = str(x)
        while not int(s[-1]):
            s = s[:-1]
        if s[0]=="-": rx = int("-"+(s[1:][::-1]))
        else: rx = int(s[::-1])
        if -2147483648<=rx<2147483647: return rx
        return 0

        #Runtime: ≈11ms | >87.77%
        #Memory : ≈11.71mb | > 11.25%