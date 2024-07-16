"""
20. Valid Parentheses
Easy
Topics
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

def isValid(s):
    stack = []
    # Mapping of closing brackets to their corresponding opening brackets
    bracket_map = {")": "(", "}": "{", "]": "["}

    for bracket in s:
        if bracket in bracket_map.values():
            # If the bracket is an opening bracket, push it to the stack
            stack.append(bracket)
        else:
            # If the stack is empty or the top of the stack is not the matching opening bracket
            if not stack or stack[-1] != bracket_map[bracket]:
                return False
            # Otherwise, pop the stack since it's a matching pair
            stack.pop()

    # If the stack is empty, all brackets were matched and the string is valid
    return len(stack) == 0

print(isValid("()"))