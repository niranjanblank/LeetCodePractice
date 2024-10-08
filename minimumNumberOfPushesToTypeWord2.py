"""
3016. Minimum Number of Pushes to Type Word II
Solved
Medium
Topics
Companies
Hint
You are given a string word containing lowercase English letters.

Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .

It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to find the minimum number of times the keys will be pushed to type the string word.

Return the minimum number of pushes needed to type word after remapping the keys.

An example mapping of letters to keys on a telephone keypad is given below. Note that 1, *, #, and 0 do not map to any letters.




Example 1:


Input: word = "abcde"
Output: 5
Explanation: The remapped keypad given in the image provides the minimum cost.
"a" -> one push on key 2
"b" -> one push on key 3
"c" -> one push on key 4
"d" -> one push on key 5
"e" -> one push on key 6
Total cost is 1 + 1 + 1 + 1 + 1 = 5.
It can be shown that no other mapping can provide a lower cost.
Example 2:


Input: word = "xyzxyzxyzxyz"
Output: 12
Explanation: The remapped keypad given in the image provides the minimum cost.
"x" -> one push on key 2
"y" -> one push on key 3
"z" -> one push on key 4
Total cost is 1 * 4 + 1 * 4 + 1 * 4 = 12
It can be shown that no other mapping can provide a lower cost.
Note that the key 9 is not mapped to any letter: it is not necessary to map letters to every key, but to map all the letters.
"""

def minimumPushes(word):
    # calculate the frequency of each letters
    freq = {}

    for char in word:
        freq[char] = freq.get(char, 0) + 1

    min_cost = 0
    for i, (char, count) in enumerate(sorted(freq.items(), key=lambda item: item[1], reverse=True)):
        # assuminng 0-7 represent 2-9 in the keypad
        # here we are using only 8 keys from the keypad which are represented by indices from 0-7
        # if all those keys are already mapped to certain keys, they will again be mapped to it but by increasing key presses
        # for the first 8 distinct chars the key press will be 1, and the next 8 character will be increased by 1 and so on
        key_presses = (i // 8) + 1

        # calculating the min_cost
        min_cost += key_presses * count

    return min_cost
