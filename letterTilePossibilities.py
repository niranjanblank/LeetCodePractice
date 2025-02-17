"""
1079. Letter Tile Possibilities
Solved
Medium
Topics
Companies
Hint
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1
 

Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""

class Solution1:
    def numTilePossibilities(self, tiles: str) -> int:
        # Time Complexity: O(n * n!) 
        # Space Complexity: O(n!) # Uses extra O(n^2) space due to remaining[:i]+remaining[i+1:]

        seq = set()
        def backtrack(curr, remaining):
            if curr not in seq and curr != "":
                seq.add(curr)
            
            if len(remaining) == 0:
                return

            for i in range(len(remaining)):
                curr += remaining[i]
                backtrack(curr,remaining[:i]+remaining[i+1:])
                curr = curr[:-1]

        backtrack("",tiles)

        return len(seq)

class Solution2:
    def numTilePossibilities(self, tiles: str) -> int:
        # Time Complexity: O(n * n!) 
        # Space Complexity: O(n!)
        seq = set()
        used = [False] * len(tiles)
        def backtrack(curr):
            if curr and curr not in seq:
                seq.add(curr)

            for i in range(len(tiles)):
                if not used[i]:
                    used[i] = True
                    backtrack(curr+tiles[i])
                    used[i] = False

        backtrack("")

        return len(seq)
            

            
            
