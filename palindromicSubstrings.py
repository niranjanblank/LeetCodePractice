"""
647. Palindromic Substrings
Medium
Topics
Companies
Hint
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:

        palin_counter = 0

        #
        def palindrome_count(left, right):
            res = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # if we here, we have encountered a palindrome
                res += 1
                left -= 1
                right += 1
            return res

        for i in range(len(s)):
            # count odd length
            palin_counter += palindrome_count(i, i)

            # count even length
            palin_counter += palindrome_count(i, i + 1)

        return palin_counter