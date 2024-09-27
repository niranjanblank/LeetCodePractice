"""
191. Number of 1 Bits
Easy
Topics
Companies
Write a function that takes the binary representation of a positive integer and returns the number of
set bits
 it has (also known as the Hamming weight).



Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

Example 3:

Input: n = 2147483645

Output: 30

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.



Constraints:

1 <= n <= 231 - 1


Follow up: If this function is called many times, how would you optimize it?
"""


class Solution1:
    # Time Complexity is O(32) as we have 32 bits
    def hammingWeight(self, n: int) -> int:
        count = 0
        # until we reach 0
        while n:
            count += n % 2
            # bitwise shift by 1
            n = n >> 1

        return count


class Solution2:
    # Time Complexity is O(32) as we have 32 bits
    def hammingWeight(self, n: int) -> int:
        count = 0
        # until we reach 0
        while n:
            # The expression n & (n - 1) clears the lowest set bit in n.
            # This means that in each iteration, the number of set bits decreases by one.
            # As a result, the number of iterations is equal to the number of set bits in n.
            # this removes the last 1 bit from the number
            """
            E.g.
            1101
           &1100
            ----
            110[0] <- 1 bit removed and changed to 0
           &1010
            ----
            1[0]00 <- 1 bit removed and changed to 0
           &0111
            ----
            [0]000 <- 1 bit removed and changed to 0
            """
            n = n & (n - 1)
            count += 1

        return count
