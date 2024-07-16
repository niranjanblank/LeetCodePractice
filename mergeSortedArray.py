"""
88. Merge Sorted Array
Easy
Topics
Companies
Hint
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
"""

def merge(nums1, m, nums2, n):
    # Initialize pointers:
    # p is the pointer for the position to insert in nums1, starting from the end.
    p = m + n - 1
    # p2 is the pointer for the current element in nums2.
    p2 = n - 1
    # p1 is the pointer for the current element in nums1 that needs to be compared.
    p1 = m - 1  # Correctly point to the last non-placeholder element in nums1.

    # While there are elements to compare in both nums1 and nums2.
    while p1 >= 0 and p2 >= 0:
        # If the current element in nums1 is larger than in nums2,
        # place it at the current position pointed by p in nums1.
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1  # Move the nums1 pointer to the left.
        else:
            # Otherwise, the current element in nums2 is larger,
            # so place it at the current position in nums1.
            nums1[p] = nums2[p2]
            p2 -= 1  # Move the nums2 pointer to the left.
        p -= 1  # Move the insert position in nums1 to the left.

    # If there are remaining elements in nums2 (meaning nums1 elements are exhausted),
    # copy them directly to nums1. This loop is only needed if nums2 has smaller elements left.
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1  # Move the nums2 pointer to the left.
        p -= 1  # Move the insert position in nums1 to the left.


def merge_bad(nums1,m,nums2,n):
    p = m

    for item in nums2:
        nums1[p] = item
        p = p + 1
    nums1.sort()
    print(nums1)
merge_bad(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
