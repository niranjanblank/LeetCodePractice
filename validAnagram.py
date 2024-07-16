"""
242. Valid Anagram
Easy
Topics
Companies
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

# method 1
def anagram(s,t):

    if len(s)!= len(t):
        return False
    s_hashmap = {}
    t_hashmap = {}

    for item in s:
        s_hashmap[item] = s_hashmap.get(item,0) + 1

    for item in t:
        t_hashmap[item] = t_hashmap.get(item,0) + 1

    return s_hashmap==t_hashmap

# method 2
def anagram_2(s,t):
    if len(s) != len(t):
        return False
    s_hashmap = {}
    t_hashmap = {}

    for i in range(len(s)):
        s_hashmap[s[i]] = s_hashmap.get(s[i],0) + 1
        t_hashmap[t[i]] = t_hashmap.get(t[i],0) + 1

    return s_hashmap == t_hashmap

print(anagram_2('anagram','nagaram'))