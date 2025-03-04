"""
1780. Check if Number is a Sum of Powers of Three
Solved
Medium
Topics
Companies
Hint
Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.

 

Example 1:

Input: n = 12
Output: true
Explanation: 12 = 31 + 32
Example 2:

Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34
Example 3:

Input: n = 21
Output: false
 

Constraints:

1 <= n <= 107
"""

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # Time Complexity: O(log3(n))
        # Space Complexity: O(1)
        while n > 0:
            if n%3 == 2:
                return False
            n = n // 3
       
        return True

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # Time Complexity : O(2^(log3(n))
        # Space Complexity: O(n)
        def backtrack(i, curr_sum):
            if curr_sum == n:
                return True
            if curr_sum > n or 3**i>n:
                return False
            # use it
            if backtrack(i+1,curr_sum+pow(3,i)):
                return True
            # dont use it
            return backtrack(i+1,curr_sum)

        return backtrack(0,0)
