"""
3. Longest Substring Without Repeating Characters
Medium
Topics
Companies
Hint
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

def lengthOfLongestSubstring(s):
    left = 0
    charSet = set()
    res = 0
    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left+=1
        charSet.add(s[right])
        res = max(res, right - left + 1)
    return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # this pointer will be used for checking repeating char
        left = 0
        # the unique characters will be saved here
        char = set()

        # current max
        max_length = 0

        # now we slide our right pointer
        for right in s:
            # if char at right is already in the window, we remove all the character upto it (i.e. from left) and update out pointer
            while right in char:
                char.remove(s[left])
                left += 1
            # add this to the currrent window of char
            char.add(right)
            max_length = max(max_length, len(char))

        return max_length