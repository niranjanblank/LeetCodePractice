"""
1306. Jump Game III
Solved
Medium
Topics
Companies
Hint
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 
Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3
Example 3:

Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.
 

Constraints:

1 <= arr.length <= 5 * 104
0 <= arr[i] < arr.length
0 <= start < arr.length
"""
class SolutionBFS:
    def canReach(self, arr: List[int], start: int) -> bool:
        # Time Complexity : O(n)
        # Space Complexirt : O(n)
        queue = deque()
        queue.append(start)

        visited = set()
        visited.add(start)

        while queue:
            for _ in range(len(queue)):
                index = queue.popleft()

                # check if we have found 0
                if arr[index] == 0:
                    return True
                left = index - arr[index]
                right = index + arr[index]
                if (left>=0) and (left not in visited):
                    queue.append(left)
                    visited.add(left)
                if (right < len(arr)) and (right not in visited):
                    queue.append(right)
                    visited.add(right)
            
        return False

class SolutionDFS:
    def canReach(self, arr: List[int], start: int) -> bool:
        # Time Complexity : O(n)
        # Space Complexirt : O(n)

        visited = set()
        self.res = False
        def dfs(index):
            
            if self.res or (index < 0 or index >= len(arr)) or (index in visited):
                return
            if arr[index] == 0:
                self.res = True        
                return 
            
           
            visited.add(index)
           
            dfs(index - arr[index])
            dfs(index + arr[index])
        
        dfs(start)
        return self.res
