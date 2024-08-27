"""
1046. Last Stone Weight
Easy
Topics
Companies
Hint
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.



Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
Example 2:

Input: stones = [1]
Output: 1


Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""
import heapq


class Solution:
    def lastStoneWeight(self, stones) -> int:
        # since heap in heapq is a minheap, we convert every item in stones to negative before creating a heap out of it
        self.heap = [-stone for stone in stones]
        # now we create a heap out of it, and at [0] index we would have the largest value but with negative sign
        heapq.heapify(self.heap)

        while len(self.heap) >= 1:
            if len(self.heap) == 1:
                return abs(self.heap[0])

            first_num = heapq.heappop(self.heap)
            second_num = heapq.heappop(self.heap)

            if first_num - second_num != 0:
                heapq.heappush(self.heap, -abs(first_num-second_num))

        return 0


class Solution2:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # since heap in heapq is a minheap, we convert every item in stones to negative before creating a heap out of it
        stones = [-stone for stone in stones]
        # now we create a heap out of it, and at [0] index we would have the largest value but with negative sign
        heapq.heapify(stones)

        while len(stones) > 1:
            first_num = heapq.heappop(stones)
            second_num = heapq.heappop(stones)
            # making sure that both stones are not same
            # if they are same, they destroy each other
            # if not the remaining weight is added to heap
            if second_num > first_num:
                heapq.heappush(stones, first_num - second_num)

        if len(stones) > 0:
            return abs(stones[0])
        return 0