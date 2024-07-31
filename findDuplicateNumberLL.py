"""
287. Find the Duplicate Number
Medium
Topics
Companies
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.



Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3


Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
"""

# O(n) space complexity
def findDuplicate(nums):
    data = set()

    for num in nums:
        if num in data:
            return num

# find the duplicate number in O(n)

def findDuplicate(nums):
    # Initialize two pointers, slow and fast, both starting at the first element of the list
    slow, fast = 0, 0

    # First phase of Floyd's Tortoise and Hare algorithm to find the intersection point
    while True:
        slow = nums[slow]  # Move the slow pointer one step forward
        fast = nums[nums[fast]]  # Move the fast pointer two steps forward

        if slow == fast:  # If the slow and fast pointers meet, a cycle is detected
            break

    # Second phase to find the entrance to the cycle (which is the duplicate number)
    slow2 = 0
    while True:
        slow = nums[slow]  # Move the slow pointer one step forward
        slow2 = nums[slow2]  # Move the slow2 pointer one step forward

        if slow == slow2:  # When the slow and slow2 pointers meet, the duplicate number is found
            return slow