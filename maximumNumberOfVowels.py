"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.



Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
"""


def maxVowels(s, k):
    s = list(s)
    max_vowels = 0
    for i in s[0:k]:
        if i in "aeiou":
            max_vowels += 1
    current_vowels = max_vowels
    for i in range(1, len(s) - k + 1):
        if s[i - 1] in "aeiou":
            current_vowels -= 1
        if s[i + k - 1] in "aeiou":
            current_vowels += 1
        if current_vowels > max_vowels:
            max_vowels = current_vowels
    return max_vowels


print(maxVowels("leetcode", 3))
