"""
678. Valid Parenthesis String
Medium
Topics
Companies
Hint
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true


Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        # indicates the minimum possible number of left parenthesis\
        # decreses when "*" or ")" is encountered
        left_min = 0
        # indicates the maximum possible number of left parenthesis
        left_max = 0
        # decreases when ")" is encountered and increases when  "(" is encountered
        for char in s:
            if char == "(":
                left_min += 1
                left_max += 1
            elif char == ")":
                left_min -= 1
                left_max -= 1
            else:
                left_min -= 1
                left_max += 1

            # if the left_max ever turns negative, its impossible to generate valid parenthesis
            if left_max < 0:
                return False

            # if left_min is less than zero, we revert it back to 0, as "*" can be counted as empty string as well
            if left_min < 0:
                left_min = 0

        # if by the end left_min is 0, the parenthesis is valid
        return left_min == 0