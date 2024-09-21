"""
139. Word Break
Medium
Topics
Companies
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bottom up approach
        dp = [False] * (len(s) + 1)
        # setting dp[len(s)] to true, as this means the end of string
        dp[len(s)] = True
        # starting from the end of string
        for i in range(len(s) - 1, -1, -1):
            # looping through each of the word in dict
            for word in wordDict:
                # checking if we start at i and go len(word) forward
                # if we are in bound and i:i+len(word) gives word, then we can break the word

                if (i + len(word)) <= len(s) and s[i:i + len(word)] == word:
                    # we can reach the end from this position
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break

        # we return dp[0] as its value indicate if we can reach the end of string or not
        return dp[0]
