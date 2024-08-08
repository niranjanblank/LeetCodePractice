"""
84. Largest Rectangle in Histogram
Hard
Topics
Companies
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.



Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4


Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
Seen this question in a real interview before?
1/5
"""

def largestRectangleArea(heights):
    maxArea = 0
    # to hold the (index, height) of the histograms in stack
    stack = []

    #  iterating through the histograms
    for i, height in enumerate(heights):
        # start index which will be added to the stack indicating the point till where the current hist can be extended to
        start = i
        # checking is stack isnt empty and the current height is less than the top element of stack
        while stack and stack[-1][1] > height:
            # if the current height is greater than we cannot extend the stack,
            # so we pop the height from the stack and calculate area and compare it to the max area
            index, h = stack.pop()
            maxArea = max(maxArea, h * (i - index))
            start = index
        # if the current height is greater than the current top item of stack, the stack can be extended without popping
        stack.append((start, height))

    # checking the area of the remaining histograms in the stack
    for i, height in stack:
        # width of the item in the stack = len(heights)-i
        maxArea = max(maxArea, height * (len(heights) - i))

    return maxArea


print(largestRectangleArea([2,1,5,6,2,3]))