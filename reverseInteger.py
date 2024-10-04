"""
7. Reverse Integer
Medium
Topics
Companies
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
"""

class Solution:
    def reverse(self, x: int) -> int:
        # range of 32 bit
        MIN = -2147483648
        MAX = 2147483647

        res = 0
        # iterate until we have  visited entire number
        while x:
            # getting the last digit
            digit = int(math.fmod(x,10))
            # removing the last digit
            x = int(x/10)

            # checking if the current reversed integer is in the range
            # checking if res is greater than 214748364, if it is then overflow happens and return 0
            if ((res > MAX//10) or 
            # checking if the last digit is grearter than 7(which is our range)
            (res==MAX//10 and digit >= MAX % 10)):
                return 0
            
            # checking for rarnge in negative direction
            if ((res < MIN//10) or (res == MIN//10 and digit <= MIN %10)):
                return 0
            
            #else
            res = (res*10)+digit

        return res
