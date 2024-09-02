"""

Code


Testcase
Test Result
Test Result
846. Hand of Straights
Medium
Topics
Companies
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.



Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.



Constraints:

1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length


Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
"""
import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        # creating hashmap to store counts of the items in hand
        hashmap = {}

        for item in hand:
            hashmap[item] = hashmap.get(item, 0) + 1

        # creating heap to keep track of the minimum items
        min_heap = list(hashmap.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first_item = min_heap[0]

            for i in range(first_item, first_item + groupSize):
                #  if i isnt in hashmap, we cannot create a group of consecutive items
                if i not in hashmap:
                    return False
                # decreasing count of item i if its utilized
                hashmap[i] -= 1
                # if the count reaches 0, remove it from the heap
                if hashmap[i] == 0:
                    heapq.heappop(min_heap)

        return True


