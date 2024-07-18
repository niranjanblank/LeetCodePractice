"""
567. Permutation in String
Medium
Topics
Companies
Hint
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.

"""

# method 1
def checkInclusion(s1,s2):
    # if length of s1 is greater than s2, then s1 cant be substring of s2
    if len(s1) > len(s2):
        return False

    count_s1 = {}
    count_s2 = {}
    for i in range(len(s1)):
        count_s1[s1[i]] = count_s1.get(s1[i],0)+1
        count_s2[s2[i]] = count_s2.get(s2[i],0)+1
    if count_s1==count_s2:
        return True

    # traversing through the sliding window
    for i in range(len(s1),len(s2),1):

        # Add the new character to the current window
        count_s2[s2[i]] = count_s2.get(s2[i], 0) + 1
        # Remove the character that's no longer in the window
        count_s2[s2[i - len(s1)]] -= 1
        if count_s2[s2[i - len(s1)]] == 0:
            count_s2.pop(s2[i-len(s1)])

        # Compare counts of the current window to s1
        if count_s1 == count_s2:
            return True

    return False

print(checkInclusion(s1 = "ab", s2 = "eidboaoo"))