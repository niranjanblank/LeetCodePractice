"""
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # bottom up approach
        # concept:
        # we create a grid of (len(text1)+1)x(len(text2)+1)
        # if letter in text1 and text2 matches, we store 1+(value at diagonal)
        # if it doesnt match, we store the max value from right or bottom from current position
        
        # this will store the matching subsequence value for each position in grid
        # initially all the values will be 0
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        # going through each of the grid in reverse
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
        # return at 0,0 position as all the grid will be filled with maximum subsequence we can reach from that point
        return dp[0][0]
