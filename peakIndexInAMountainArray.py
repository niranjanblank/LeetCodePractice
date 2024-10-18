"""
852. Peak Index in a Mountain Array
Solved
Medium
Topics
Companies
You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity.

 

Example 1:

Input: arr = [0,1,0]

Output: 1

Example 2:

Input: arr = [0,2,1,0]

Output: 1

Example 3:

Input: arr = [0,10,5,2]

Output: 1

 

Constraints:

3 <= arr.length <= 105
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.
"""


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r = 0, len(arr)
        
        while l<=r:
            m = (l+r)//2

            # if an element has element left to it and element right to it less than current element,
            # this is the peak
            if ((m-1) >= 0 and arr[m-1]< arr[m]) and 
            ((m+1)<len(arr) and arr[m] > arr[m+1]):
                return m
            # if current element is less than right element, then it means peak must be in the right side
            elif m+1<len(arr) and arr[m] < arr[m+1]:
                l = m+1
            # if current element is less than left element, then the element is in left side
            # we can just use else case here
            elif (m-1 >=0) and arr[m-1] > arr[m]:
                r = m -1
        
