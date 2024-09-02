"""
763. Partition Labels
Medium
Topics
Companies
Hint
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.



Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]


Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
"""


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # creating a hashmap to store last index of each letter in the string
        last_index_hashmap = {}

        for i, letter in enumerate(s):
            last_index_hashmap[letter] = i

        partition_size = []
        size = 0
        end = 0

        # iterating through entire string
        for i, letter in enumerate(s):
            # increase the size after visiting the element
            size += 1
            # updating the end index to the last index of currernt letter
            end = max(end, last_index_hashmap[letter])

            # if we reach the end, then this means a partition is needed here
            if i == end:
                partition_size.append(size)
                # reset the size for next partition
                size = 0

        return partition_size
