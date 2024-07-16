"""
125. Valid Palindrome
Easy
Topics
Companies
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

# method 1 (Two pointers)
def isPalindrome(s):
    # convert to lower
    s = s.lower()
    # remove non-alphanumeric characters
    s = ''.join(filter(str.isalnum, s))

    # checking palindrome using two pointers
    start = 0
    end = len(s)-1

    while start < end:
        if s[start] != s[end]:
            return False
        start+=1
        end-=1

    return True

# method 2
def isPalindrome2(s):
    # remove non-alphanumeric characters after conversion to lower
    s = ''.join(filter(str.isalnum, s.lower()))
    return s==s[::-1]

print(isPalindrome2("asdas Av ads "))