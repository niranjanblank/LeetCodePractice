"""
1358. Number of Substrings Containing All Three Characters
Solved
Medium
Topics
Companies
Hint
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
 

Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
"""
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        strings = defaultdict(int)

        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in "abc":
                strings[s[r]]+=1

            while len(strings) == 3:
                res += len(s) - r

                strings[s[l]]-=1
                if strings[s[l]] == 0:
                    strings.pop(s[l])

                l+=1

        return res
