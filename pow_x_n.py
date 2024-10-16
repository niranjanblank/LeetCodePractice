"""
50. Pow(x, n)
Solved
Medium
Topics
Companies
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).



Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Helper function to calculate the power recursively
        def helper(x, n):
            # If base x is 0, return 0 immediately (as any power of 0 is 0)
            if x == 0:
                return 0
            # If exponent n is 0, return 1 (as any number to the power of 0 is 1)
            if n == 0:
                return 1

            # Recursively calculate power for half the exponent
            res = helper(x, n // 2)
            # Multiply the result by itself (this handles the squaring for even powers)
            res = res * res

            # If the original exponent is odd, multiply by x once more
            # Otherwise, just return the squared result
            return x * res if n % 2 else res

        # Call the helper function with the absolute value of n to handle negative exponents
        result = helper(x, abs(n))
        # If the exponent was positive, return the result directly
        # If the exponent was negative, return 1/result to handle the inverse
        return result if n >= 0 else 1 / result
