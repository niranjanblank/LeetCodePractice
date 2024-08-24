"""
208. Implement Trie (Prefix Tree)
Solved
Medium
Topics
Companies
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.


Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True


Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""

class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:

    def __init__(self):
        # root where the trie begins
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # when we insert word in a trie, we begin it at root
        curr = self.root

        for c in word:
            # if the letter is already in the trie go to the children,
            # else add it to the children and go to the children
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        # at the end of the word, consider the curr trie to be end of word
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        # search begins at root
        curr = self.root

        # iterate through each char in word
        for c in word:
            # if the letter isnt in the children, its not in the trie so return false
            if c not in curr.children:
                return False
            # if its in the children, go to the children
            curr = curr.children[c]

        # after iterating through each char, if the item is in the trie the children node will have true for endOfWord
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        # search begins at root
        curr = self.root

        # iterate through each char in word
        for c in prefix:
            # if the letter isnt in the children, its not in the trie so return false
            if c not in curr.children:
                return False
            # if its in the children, go to the children
            curr = curr.children[c]

        # if all the letter in prefix were interated without returning false, then there are words starting with prefix
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)