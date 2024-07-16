"""
22. Generate Parentheses
Medium
Topics
Companies
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""


def generateParenthesis(n):
    # This function generates all combinations of well-formed parentheses for a given number n
    # 'n' represents the number of pairs of parentheses

    stack = []  # Stack to keep track of the current state of parentheses
    res = []  # List to store all valid combinations

    def backtrack(openN, closedN):
        # This is a recursive function that performs backtracking to generate the parentheses

        if openN == closedN == n:
            # If the number of open and closed parentheses both equal n,
            # we have a valid combination, so we add it to the result
            res.append("".join(stack))
            return

        if openN < n:
            # If the number of open parentheses is less than n,
            # we can add an open parenthesis and continue the backtracking
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()  # Remove the last added parenthesis to backtrack

        if closedN < openN:
            # If the number of closed parentheses is less than the number of open ones,
            # we can add a closed parenthesis and continue the backtracking
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()  # Remove the last added parenthesis to backtrack

    backtrack(0, 0)  # Start the backtracking with 0 open and 0 closed parentheses
    return res  # Return the list of all valid combinations
print(generateParenthesis(3))