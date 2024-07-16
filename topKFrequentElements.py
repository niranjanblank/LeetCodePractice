"""
347. Top K Frequent Elements
Medium
Topics
Companies
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

def topKFrequent(nums, k):
    # O(n log n) complexity
    counts = {}
    for num in nums:
        counts[num] = counts.get(num,0) + 1
    sorted_dict = {key: value for key, value in sorted(counts.items(), key=lambda item: item[1], reverse=True)}
    return list(sorted_dict.keys())[:k]

def topKFrequent2(nums,k):
    # O(n) complexity
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    # create bucket
    buckets = [[] for _ in range(len(nums) + 1)]

    # populate each bucket where index is the frequency of element
    for key, value in counts.items():
        buckets[value].append(key)

    # get top k elements
    top_k_elements = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            top_k_elements.append(num)
            if len(top_k_elements) == k:
                return top_k_elements
print(topKFrequent2(nums = [1,1,2,2,3,3], k = 2))