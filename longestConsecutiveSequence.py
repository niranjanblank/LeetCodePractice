"""

Code
Testcase
Test Result
Test Result
128. Longest Consecutive Sequence
Medium
Topics
Companies
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

# method 1: time complexity O(nlogn)
def longestConsecutive(nums):
    if len(nums) == 0:
        return 0
    nums = sorted(list(set(nums)))
    longest_seq = 1
    temp_seq = 1
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]+1:
            temp_seq+=1
        else:
            longest_seq = max(temp_seq, longest_seq)
            temp_seq = 1

    longest_seq = max(temp_seq, longest_seq)
    return longest_seq


def longestConsecutive_best(nums):
    # Convert the list to a set to eliminate duplicates and allow O(1) average-time complexity lookups
    nums = set(nums)
    # Initialize a variable to keep track of the longest consecutive sequence found
    longest = 0

    # Iterate through each number in the set
    for item in nums:
        # Check if the current number is the start of a sequence
        if item - 1 not in nums:
            # Initialize length of the current sequence
            length = 1
            # Continue to increment the sequence length until the next consecutive number is found
            while item + length in nums:
                length += 1
            # Update the longest sequence found so far
            longest = max(length, longest)

    # Return the longest sequence found
    return longest


print(longestConsecutive_best(nums=[7,-9,3,-6,3,5,3,6,-2,-5,8,6,-4,-6,-4,-4,5,-9,2,7,0,0]))