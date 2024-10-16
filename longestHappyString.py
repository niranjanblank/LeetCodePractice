"""
1405. Longest Happy String
Solved
Medium
Topics
Companies
Hint
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
 

Constraints:

0 <= a, b, c <= 100
a + b + c > 0
"""

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # creating max heap
        items = [(-a,"a"),(-b,"b"),(-c,"c")]
        # create heap, dont add item with 0 count
        max_heap = []
        heapq.heapify(max_heap)
        for item in items:
            if item[0]!=0:
                heapq.heappush(max_heap,item)
        res = ""

        while max_heap:
            # getting item from the heap
            count, char = heapq.heappop(max_heap)
            # checking if we already have two continous character
            if len(res) > 1 and res[-1] == char and res[-2] == char:
                # if so, we need to get another element
                # if we dont have 2nd most common char, break
                if not max_heap:
                    break
                count2, char2 = heapq.heappop(max_heap)
                res+=char2
                # decrease the count
                count2+=1
                # if this item still has count remaining add it back to the max_heap
                if count2:
                    heapq.heappush(max_heap,(count2, char2))
            else:
                res+=char
                count+=1
            if count:
                heapq.heappush(max_heap,(count, char))
        return res
