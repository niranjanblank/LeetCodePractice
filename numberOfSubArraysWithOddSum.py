"""
"""
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # brute force method (TLE)
        # generate all the numberrs
        # Time Complexity : O(n^2)
        # Space Complexity: O(1)
        MOD = 1e9+7

        n = len(arr)
        count = 0
        
        for start in range(n):
            curr_sum = 0

            for end in range(start, n):
                curr_sum += arr[end]

                if curr_sum %2 != 0:
                    count+=1

        return int(count % MOD)

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        curr_sum = 0
        odd_count = 0 
        even_count = 0
        count = 0
        for num in arr:
            curr_sum += num

            if curr_sum % 2 != 0 :
                count += 1
                count += even_count
                odd_count+=1
            else:
                even_count += 1
                count+= odd_count

        return int(count%(1e9 + 7))
