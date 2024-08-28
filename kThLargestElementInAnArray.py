"""
215. Kth Largest Element in an Array
Medium
Topics
Companies
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # create heap, we are adding - for each item here to convert max item to min for the minheap to work
        heap = [-num for num in nums]
        heapq.heapify(heap)

        res = None
        for i in range(k):
            res = heapq.heappop(heap)

        return -res


class Solution2:
    # O(nlogk)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialize a min-heap
        min_heap = []
        heapq.heapify(min_heap)

        # Maintain a heap of size k
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # The root of the heap is the k-th largest element
        return min_heap[0]