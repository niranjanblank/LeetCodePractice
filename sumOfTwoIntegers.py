"""
371. Sum of Two Integers
Medium
Topics
Companies
Given two integers a and b, return the sum of the two integers without using the operators + and -.



Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5


Constraints:

-1000 <= a, b <= 1000
Seen this question in a real interview before?
1/5
"""


class Solution:

    def getSum(self, a: int, b: int) -> int:
        # this will mask out anything large than 32 bits
        mask = 0xffffffff

        while b!= 0:
            carry = (a & b) << 1
            # calc sum without carry
            a = (a ^ b) & mask
            # apply mask and carry
            b = carry & mask

        if a > mask // 2:
            return ~(a^mask)
        else:
            return a