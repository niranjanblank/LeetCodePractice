"""
309. Best Time to Buy and Sell Stock with Cooldown
Medium
Topics
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
 

Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we will store key: (i, buying)  here buying is a boolean which indicates whether we buy or sell at i
        # value: val , here val is the maximum profit at (i, buying)
        cache = {}

        def dfs(i, buying):
            # if we exceed the length of prices we return 0
            if i>=len(prices):
                return 0
            if (i, buying) in cache:
                return cache[(i,buying)]
            
            if buying:
                # if we are buying at current i, we have two choices
                # 1. buy 
                # 2. cooldown
                buy = dfs(i+1, not buying) - prices[i] # if we brought then we need do deduct the cost
                cooldown = dfs(i+1, buying)
                # store the maximum prrofit we could get thorough cooldown or buying
                cache[(i, buying)] = max(buy, cooldown)
            else:
                # here we can either sell or cooldown
                # in sell we increase i by 2 as we need 1 day cooldown
                sell = dfs(i+2, not buying) + prices[i]
                cooldown = dfs(i+1, buying)
                cache[(i, buying)] = max(sell, cooldown)
            return cache[(i, buying)]

        return dfs(0, True)
