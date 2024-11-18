"""
4. Median of Two Sorted Arrays
Solved
Hard
Topics
Companies
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
class BruteForceSolution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # time complexity: O((n+m)log(n+m)) 
        nums1 += nums2
        nums1 = sorted(nums1)
        mid = len(nums1) // 2
        if len(nums1) % 2:
            return nums1[mid]
        return (nums1[mid-1]+nums1[mid])/2

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #time complexity: O(log(min(m,n))

        A,B = nums1 , nums2
        # total items from nums1 and nums2
        total = len(A) + len(B)
        middle = total // 2
        # If A is the smaller array, the search space is minimized, making the algorithm more efficient
        if len(A) > len(B):
            A , B = B, A
        
        l,r = 0, len(A)-1
        while True:
            mid_A =  (l+r)//2
            # we do -2 to avoid off by one error, as the indexs of A and B both start with 0
            mid_B = middle - mid_A - 2
            # left section from A and B
            # if the index is less than 0, we set the left value to -infinity
            Aleft = A[mid_A] if mid_A >= 0 else float("-infinity")
            Bleft = B[mid_B] if mid_B >= 0 else float("-infinity")
            # right section from A and B
            # if the index is greater than length of array, we set the left value to infinity
            Aright = A[mid_A+1] if mid_A+1 < len(A) else float("infinity")
            Bright = B[mid_B+1] if mid_B+1 <len(B) else float("infinity")

            ## checking if we have median
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright,Bright)

                # maximum of Aleft is the mid item , and min of Aright Bright is the mid+1 item for the median formula
                return (max(Aleft, Bleft)+min(Aright, Bright))/2
            elif Aleft > Bright:
                # this means the mid value doesnt belong to the left section
                r = mid_A - 1
            else:
                l = mid_A + 1


