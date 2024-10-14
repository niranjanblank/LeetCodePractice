"""
202. Happy Number
Solved
Easy
Topics
Companies
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1
"""
# time complexity is O(logn) for both the solution
class Solution:
    def isHappy(self, n: int) -> bool:
        # to keep track of the numbers that have already been processed
        seen = set()

        # loop will end when we find 1 as result, or we detect a cycle
        while n!=1 and n not in seen:
            # add n to seen set
            seen.add(n)
            # to keep track of the result
            res = 0
            # we continue this loop until we have processed all the digits
            while n!=0:
                digit = n % 10
                res += digit ** 2
                n = n // 10
            n = res
        
        return n == 1

class Solution2:
    def isHappy(self, n: int) -> bool:
        # slow and fast pointer method to check for cycle
        # if at some point if slow and fast pointer meet, there exists a cycle
        slow, fast = n , self.sum_of_squares(n)

        # loop will end when we find 1 as result, or we detect a cycle
        # we check fast!=1 as fast reaches the destination faster as its going twice the speed
        while fast!=1 and slow!=fast:
            # fast pointer moves twice at a time and slow moves one at a time
            fast = self.sum_of_squares(fast)
            fast = self.sum_of_squares(fast)
            slow = self.sum_of_squares(slow)
        return fast == 1

    def sum_of_squares(self, n):
        res = 0
        while n!=0:
            digit = n % 10
            res += digit ** 2
            n = n // 10
        return res
