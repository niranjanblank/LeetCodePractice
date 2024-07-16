"""
739. Daily Temperatures
Medium
Topics
Companies
Hint
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.



Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]


Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
Seen this question in a real interview before?
1/5
"""

# inefficient
def dailyTemperatures1(temperatures):
    answer = []
    for i in range(len(temperatures)):
        steps = 1
        for j in range(i+1, len(temperatures)):
            if temperatures[j]>temperatures[i]:
                answer.append(steps)
                break
            else:
                steps += 1

            if j+1 >= len(temperatures):
                steps=0
                answer.append(steps)
    answer.append(0)
    return answer

# monotonic stack
def dailyTemperatures(temperatures):
    # Initialize a list to store the results with default value 0
    output = [0] * len(temperatures)
    # Initialize a stack to keep track of temperatures and their indices
    stack = []
    # Iterate through the list of temperatures
    for i, t in enumerate(temperatures):
        # While stack is not empty and current temperature is higher than the temperature at the top of the stack
        while stack and t > stack[-1][0]:
            # Pop the temperature and its index from the stack
            stackT, stackInd = stack.pop()
            # Calculate the number of days until a warmer temperature and store it in the output list
            output[stackInd] = i - stackInd
        # Append the current temperature and its index to the stack
        stack.append([t, i])
    return output

print(dailyTemperatures([73,74,75,71,69,72,76,73]))
