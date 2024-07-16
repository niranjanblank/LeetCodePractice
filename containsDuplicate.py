"""
217. Contains Duplicate
Easy
Topics
Companies
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

"""

# method 1
def containsDuplicate(nums):
    return len(nums)!= len(list(set(nums)))

#method 2
def containsDuplicate_Hash(nums):
    hash_nums = {}
    for item in nums:
        hash_nums[item] = hash_nums.get(item,0)+1
        if hash_nums[item]>1:
            return True
    return False

#method 3
def containsDuplicate_3(nums):
    # Initialize an empty set to keep track of the numbers we've seen so far.
    seen = set()

    # Iterate over each number in the list 'nums'.
    for num in nums:
        # Check if the current number is already in the set 'seen'.
        if num in seen:
            # If it is, that means we've found a duplicate.
            return True
        # If the current number is not in the set, add it to the set.
        seen.add(num)

    # If we finish the loop and haven't returned True, it means there are no duplicates.
    return False
print(containsDuplicate_3([1,1,1,3,3,4,3,2,4,2]))