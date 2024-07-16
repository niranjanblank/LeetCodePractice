"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.



Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""


def longestOnes(nums, k):
    left = 0  # Initialize the left boundary of the sliding window
    zero_count = 0  # Initialize the count of zeros within the window
    max_length = 0  # Initialize the maximum length of valid window found

    # Iterate through each element in nums with 'right' as the right boundary of the window
    for right in range(len(nums)):
        # If the current element is 0, increment the zero count
        if nums[right] == 0:
            zero_count += 1

        # If the zero count exceeds k, shrink the window from the left
        while zero_count > k:
            # If the leftmost element is a 0, decrement the zero count
            if nums[left] == 0:
                zero_count -= 1
            # Move the left boundary of the window to the right
            left += 1

        # Update max_length with the maximum between the previous max_length and the size of the current window
        max_length = max(max_length, right - left + 1)

    # Once the loop is complete, return the maximum length found
    return max_length


print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
