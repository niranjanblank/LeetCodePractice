"""
338. Counting Bits
Easy
Topics
Companies
Hint
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.



Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101


Constraints:

0 <= n <= 105


Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""


class Solution:
    def countBits(self, n: int) -> List[int]:
        # initializE the numbers of 1 forr each of the n+1 elements to be 0
        dp = [0] * (n + 1)

        # first power of 1
        # following this formula dp[i] = 1 + dp[i-offset] , offset is the position of most significant bit
        offset = 1
        for i in range(1, n + 1):
            # checking if we have reached a new significant bit
            if offset * 2 == i:
                offset = i

            # calculating the number of bits
            dp[i] = 1 + dp[i - offset]

        return dp
