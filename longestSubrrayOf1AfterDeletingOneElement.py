# def longestSubarray(nums):
#     left = 0
#     max_length = 0
#     element_count = 0
#     for right in range(len(nums)):
#         if nums[right]==0:
#             element_count+=1
#         while element_count > 1:
#             if nums[left]==0:
#                 element_count-=1
#             left+=1
#         max_length = max(max_length,right-left)
#     return max_length

def longestSubarray(nums):
    max_len = 0  # to track the maximum length of subarray
    zero_index = -1  # to keep track of the last zero's index
    left = 0  # left pointer for the window

    for right in range(len(nums)):
        if nums[right] == 0:
            left = zero_index + 1  # Move the left pointer right after the last zero
            zero_index = right  # Update the last zero's index
        max_len = max(max_len, right - left)  # Update the max length of the subarray

    return max_len
print(longestSubarray([1,1,1]))