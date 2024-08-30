"""
17. Letter Combinations of a Phone Number
Medium
Topics
Companies
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.




Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]


Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def dfs(i, curr_string):
            # checking if the string contains element from all the digits
            if len(curr_string) == len(digits):
                # if all keys are pressed
                res.append(curr_string)
                return

            # now we go through each of the char
            for c in digit_to_char[digits[i]]:
                dfs(i + 1, curr_string + c)

        if digits:
            dfs(0, "")
        return res