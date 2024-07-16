"""
122. Best Time to Buy and Sell Stock II
Medium
Topics
Companies
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
"""


def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        # If the current price is higher than the previous one, add the difference to the profit.
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit


def maxProfit2(prices):
    profit = 0
    buy_point = 0
    for i in range(1, len(prices)):
        # Check if the current price is less than the next price (indicating a rise in stock prices)
        if prices[i] > prices[buy_point]:
            # If the current price is the last price or the next price is lower, sell the stock
            if i == len(prices) - 1 or prices[i + 1] < prices[i]:
                profit += prices[i] - prices[buy_point]
                buy_point = i + 1  # Update the buy_point to the day after selling
        else:
            buy_point = i  # Update buy_point if current day's price is lower than the previous buy_point
    return profit

print(maxProfit2([2, 4, 1]))
