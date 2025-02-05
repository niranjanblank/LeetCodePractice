"""
1790. Check if One String Swap Can Make Strings Equal
Solved
Easy
Topics
Companies
Hint
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
 

Constraints:

1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
"""

class Solution1:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        if s1 == s2: 
            return True
       
        mis_match = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                mis_match.append((s1[i],s2[i]))
                if len(mis_match) > 2:
                    return False
        return len(mis_match)==2 and mis_match[0]  == mis_match[1][::-1]

class Solution2:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
     
        if s1 == s2:
            return True
        diff_count = 0
        s1_letters = []
        s2_letters = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_count +=1
                s1_letters.append(s1[i])
                s2_letters.append(s2[i])
                if diff_count > 2:
                    return False
     
        return sorted(s1_letters) == sorted(s2_letters)
