"""
"""


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # Time Complexity: O((r-l+1)* n)
        # Space: O(1)
        min_sum = float("inf")
        n = len(nums)
        for size in range(l,r+1):
            curr_sum = sum(nums[:size])
            if curr_sum > 0:
                    min_sum = min(curr_sum, min_sum)
             # Slide the window across the array
            for j in range(size, n):  # O(n - size)
                curr_sum += nums[j] - nums[j - size]  # O(1) update
                
                # Check if it's a valid subarray sum
                if curr_sum > 0:
                    min_sum = min(min_sum, curr_sum)

        return min_sum if min_sum != float("inf") else -1
