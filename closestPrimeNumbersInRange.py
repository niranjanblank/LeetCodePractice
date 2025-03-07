"""
2523. Closest Prime Numbers in Range
Solved
Medium
Topics
Companies
Hint
Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= num1 < num2 <= right .
Both num1 and num2 are prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

 

Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.
Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
 

Constraints:

1 <= left <= right <= 106
"""

class Solution:
    def is_prime(self,num):
        # Time Complexity: O(n/2) = O(n)
        if num == 1:
            return False
        
        if num == 2 or num ==3:
            return True 
        for i in range(2,num//2+1):
            if num % i == 0:
                return False
        return True

    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        prev_prime = -1
        num1 = -1
        num2 = -1
        min_diff = float("inf")
        # generate all the primes in the range
        for num in range(left, right+1):
            if self.is_prime(num):
                if prev_prime != -1:
                    curr_diff = num - prev_prime
                    if curr_diff < min_diff:
                        min_diff = curr_diff
                        num1 = prev_prime
                        num2 = num
                    #Return immediately if the smallest possible prime gap (1 or 2) is found
                    if curr_diff == 1 or curr_diff == 2:
                        return [prev_prime, num]
                prev_prime = num
            
        return [num1,num2] if num1 != -1 else [-1,-1]
