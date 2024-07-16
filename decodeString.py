"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.



Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"


Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""

def decodeString(s):
    stack = []  # Stack to keep track of previous strings and numbers
    curr_string = ""  # Current string being formed
    curr_num = 0  # Current number being formed

    # Iterate through each character in the string
    for c in s:
        if c.isdigit():
            # If the character is a digit, build the current number
            # Multiple digits may form a number, hence multiply by 10 for each new digit
            curr_num = curr_num * 10 + int(c)
        elif c == "[":
            # If '[' is encountered, it indicates the start of an encoded string
            # Push the current string and number onto the stack
            # This helps to return to the previous state after completing the inner string
            stack.append((curr_string, curr_num))
            # Reset the current string and number for the new encoded string
            curr_string = ""
            curr_num = 0
        elif c == "]":
            # If ']' is encountered, it indicates the end of an encoded string
            # Pop the last string and number from the stack
            # This restores the previous state (string before the '[')
            prev_string, prev_num = stack.pop()
            # Repeat the current string 'prev_num' times and append it to 'prev_string'
            # This forms the new current string
            curr_string = prev_string + prev_num * curr_string
        else:
            # For normal characters, append them to the current string
            curr_string += c
        print(stack, curr_string)
    # Return the fully decoded string
    return curr_string
print(decodeString("3[a2[c]][bc]"))