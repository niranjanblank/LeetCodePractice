"""
49. Group Anagrams
Medium
Topics
Companies
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

"""

#O(n⋅klogk)
def groupAnagrams(strs):
    # Dictionary to hold the groups of anagrams
    anagrams = {}

    # transverse through each word in the list
    for word in strs:
        # sort the word to get the key
        sorted_word = "".join(sorted(word))

        # If the key is in the dictionary, append the word to the corresponding list
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            #  otherwise, create a new entry with this sorted word as the key
            anagrams[sorted_word] = [word]

    # Rturn the groups of anagrams collected in the dictionary values
    return list(anagrams.values())


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))