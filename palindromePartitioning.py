"""
131. Palindrome Partitioning
Medium
Topics
Companies
Given a string s, partition s such that every
substring
 of the partition is a
palindrome
. Return all possible palindrome partitioning of s.



Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]


Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
"""


class Solution:

    def palindrome(self, value):
        """Method to check for palindrome using two pointers"""
        left, right = 0, len(value) - 1
        while left < right:
            if value[left] != value[right]:
                return False
            left += 1
            right -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        # To store the overall result
        res = []

        # To store the current partition of palindromes
        part = []

        def dfs(i):
            # When we reach the end of the string, add the current partition to the result
            if i >= len(s):
                res.append(part.copy())
                return

            # Go through each possible partition
            for j in range(i, len(s)):
                # If the current substring is a palindrome, explore further partitions

                # For example:
                # Given the string "aab", the loop will consider substrings like "a", "aa", and "aab".
                # If "a" (from s[i:j+1] where i=0 and j=0) is found to be a palindrome,
                # it will be added to the current partition, and the algorithm will then
                # recursively explore the remaining substring "ab".
                # The process continues, checking substrings within "ab", and so on.
                if self.palindrome(s[i:j + 1]):
                    part.append(s[i:j + 1])  # Add the palindrome substring to the current partition
                    dfs(j + 1)  # Recur to explore further partitions
                    part.pop()  # Backtrack to explore other partitions

        dfs(0)

        return res

