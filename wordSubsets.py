"""
916. Word Subsets
Solved
Medium
Topics
Companies
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

 

Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]

Output: ["facebook","google","leetcode"]

Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lc","eo"]

Output: ["leetcode"]

Example 3:

Input: words1 = ["acaac","cccbb","aacbb","caacc","bcbbb"], words2 = ["c","cc","b"]

Output: ["cccbb"]

 

Constraints:

1 <= words1.length, words2.length <= 104
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.
"""

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        #Time Complexity: O(mo+np+mu)
        # Space Complexity: O(mo + u)

        words1_dict = defaultdict(dict)
        words2_dict = defaultdict(int)
        res = []
        # O(mxo) # p is average length of word or largest length
        # save count of each letter for each of the words
        for word in words1:
            for letter in word:
                words1_dict[word][letter] = words1_dict[word].get(letter,0) + 1

        # O(nxp) # p is average length of word or largest length
        # save the maximum count of letters for all the unique letters in words2
        for word in words2:
            tmp_dict = defaultdict(int)
            for letter in word:
                tmp_dict[letter]+=1
            for char, freq in tmp_dict.items():
                words2_dict[char] = max(words2_dict[char], freq)
     
        # O(mu) # u = unique chars in the dict
        for w1 in words1:
            includes = True
            for char,freq in words2_dict.items():
                # if for any word, we dont have equal or greater count for rerspective char, it wont be included
                # e.g amazon{a:2,m:1,z:1,o:1,n:1}, aaan:{a:3,t:1} 
                # here amazon has 2 a, but aaan has 3 a, so if we get such case, it wont be included in the result
                if words1_dict[w1].get(char,0) < freq:
                    includes = False
                    break
            if includes:
                res.append(w1)
     
        return res
