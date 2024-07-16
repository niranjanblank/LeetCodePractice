"""
80. Remove Duplicates from Sorted Array II
Medium
Topics
Companies
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.



Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""

def removeDuplicates(nums):
    write=0
    read=1
    curr = nums[0]
    count = 1
    while read < len(nums):

        if curr==nums[read]:
            read+=1
            count+=1
        else:
            if count > 2: count=2
            while count>0:
                nums[write] = curr
                write+=1
                count-=1
            curr = nums[read]

    else:
        if count > 2: count = 2
        while count > 0:
            nums[write] = curr
            write += 1
            count -= 1

    print(nums)
    print(write)

def removeDuplicatesBetter(nums):
    # The initial write position should be 2, assuming the first two positions
    # are always valid because each element can appear at least twice.
    write = 2

    for read in range(2, len(nums)):
        # We only write the current reading element if it's not the same as
        # the element two positions before it in the array. This effectively
        # skips over duplicates beyond the second occurrence.
        if nums[read] != nums[write - 2]:
            nums[write] = nums[read]
            write += 1

    # The write pointer now points to the position after the last valid element,
    # which coincides with the length of the array without extra duplicates.
    return write

removeDuplicatesBetter([1,1,2,2,2,3])

removeDuplicates([1,1,2,2,2,3])

