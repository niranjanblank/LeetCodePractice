# def findDifference(nums1, nums2):
#     nums1 = list(set(nums1))
#     nums2 = list(set(nums2))
#     for item in nums1.copy():
#         if item in nums2:
#             nums1.remove(item)
#             nums2.remove(item)
#     return [nums1, nums2]

# def findDifference(nums1, nums2):
#     nums1 = set(nums1)
#     nums2 = set(nums2)
#
#     item_list_1 = list(nums1 - nums2)
#     item_list_2 = list(nums2 - nums1)
#     return [item_list_1, item_list_2]

# hashtables
def findDifference(nums1, nums2):
    hash1, hash2 = {}, {}

    # creating hash for the items
    for item in nums1:
        hash1[item] = hash1.get(item,0) + 1
    for item in nums2:
        hash2[item] = hash2.get(item,0) + 1
    list_1 = [item for item in hash1 if item not in hash2]
    list_2 = [item for item in hash2 if item not in hash1]

    return [list_1, list_2]
print(findDifference([1,2,3,3],[1,1,2,2]))