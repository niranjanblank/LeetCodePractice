"""
"""
class Solution:
    # Time Complexity: O(nklogx)
    # Space Complexity: O(n)
    def xSum(self, array, x):
        values = {}
        for item in array:
            data = values.get(item,[0,item])
            values[item] = [data[0]+1, item]

        # sorting 
        sorted_values = sorted(values.values(), key=lambda x: (-x[0],-x[1]))
        x_sum = 0
        for item in sorted_values[:x]:
            x_sum += item[0]*item[1]

        return x_sum
        
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        l,r = 0,k
        while r <= len(nums):
            ans = self.xSum(nums[l:r],x)
            res.append(ans)
            l+=1
            r+=1

        return res
