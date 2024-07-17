"""
424. Longest Repeating Character Replacement
Medium
Topics
Companies
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.



Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.


Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""
# solution 1
def chararcterReplacement(s, k):
    left = 0
    right = 0
    counts = {}
    res = 0
    while  right < len(s):

        counts[s[right]] = counts.get(s[right],0) + 1
        window_len = right - left + 1
        max_v = max(counts.values())
        if window_len - max_v <= k:
            res = max(res, window_len)

        else:
            counts[s[left]] = counts[s[left]] - 1
            left+=1
        right += 1
    return res

# solution 2
def characterReplacement2(s,k):
    left = 0
    counts = {}
    res = 0

    for right in range(len(s)):
        counts[s[right]] = counts.get(s[right], 0) + 1

        # until the window becomes valid, we increase the left
        while (right - left + 1) - max(counts.values()) > k:
            counts[s[left]]-=1
            left+=1
        res = max(res, right - left + 1)
    return res
print(chararcterReplacement(s = "AABABBA", k = 1))