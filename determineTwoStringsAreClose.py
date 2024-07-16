"""
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.



Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"


Constraints:

1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.
"""

def closeStrings(word1, word2):
    word1 = list(word1)
    word2 = list(word2)
    if len(word1) != len(word2):
        return False

    unique_freq_1, unique_freq_2 =  {}, {}
    for letter in word1:
        unique_freq_1[letter] = unique_freq_1.get(letter, 0) + 1
    for letter in word2:
        unique_freq_2[letter] = unique_freq_2.get(letter, 0) + 1

    if (sorted(unique_freq_1.keys())!=sorted(unique_freq_2.keys())) or \
            (sorted(unique_freq_1.values())!= sorted(unique_freq_2.values())):
        return False
    return True

print(closeStrings("abc","bca"))