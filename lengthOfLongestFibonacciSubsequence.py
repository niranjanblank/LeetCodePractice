"""
"""
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # Time Complexity: O(n^2 * logm)
        # Space Complexity: O(n)
        hashset = set(arr)
        max_len = 0
        
        for start in range(len(arr)):
            for end in range(start+1,len(arr)):
                count = 2
                prev = arr[start]
                curr = arr[end]
                nxt =  prev + curr
                while  nxt in hashset:
                    # A Fibonacci sequence grows logarithmically relative to the input size, meaning its length is at most O(log M), where 
                    # M is the maximum possible value in arr
                    prev = curr
                    curr = nxt
                    nxt = prev + curr
                    count += 1
                    max_len = max(max_len, count)

        return max_len
