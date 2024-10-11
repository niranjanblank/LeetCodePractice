"""

Code


Testcase
Test Result
Test Result
1539. Kth Missing Positive Number
Solved
Easy
Topics
Companies
Hint
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length
 

Follow up:

Could you solve this problem in less than O(n) complexity?
"""


class Solution1:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        curr_number = 0
        missing_count = 0
        
        # Loop through the range 1 to arr[-1]
        for i in range(1, arr[-1] + 1):
            if curr_number < len(arr) and i == arr[curr_number]:
                curr_number += 1
            else:
                missing_count += 1
                if missing_count == k:
                    return i
        
        # If we haven't found the kth missing within the array range,
        # we need to account for numbers beyond arr[-1]
        return arr[-1] + (k - missing_count)

class Solution2:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        curr_number = 1
        missing_count = 0
        index = 0
        while missing_count < k:
            if index < len(arr) and arr[index] == curr_number:
                index += 1
            else:
                # the curr_number at this point is the kth missing number
                missing_count+=1

            curr_number += 1
        # decrease by one, as we have increased curr_number when we increased k
        return curr_number - 1
