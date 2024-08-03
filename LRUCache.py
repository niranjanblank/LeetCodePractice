"""
146. LRU Cache
Medium
Topics
Companies
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.



Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        # prev and next to create a doubly linked list
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        # hashmap to store the value of the keys
        self.cache = {}

        # left links to LRU, right links to MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        # initially linking these nodes, and all the new nodes will be added in between
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        # remove the node from anywhere within the linked list
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        # add the node at the right, which represents the most recently used
        prev = self.right.prev

        prev.next = node
        # setting the prev and next of this node
        node.prev = prev
        node.next = self.right

        self.right.prev = node

    def get(self, key: int) -> int:
        # checking if its in the cache:
        if key in self.cache:
            # if we get it, then its the most recently used, so we need to remove it from its position and add at the right
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            # getting the val from the cache
            return self.cache[key].val
        # if its not in the cache then return -1
        return -1

    def put(self, key: int, value: int) -> None:
        # putting at the right most
        # if it already exists in the cache, we first remove it from the linked list and make it the most recent the prev value and add it in the cache
        if key in self.cache:
            self.remove(self.cache[key])
        # create a new node with this value
        self.cache[key] = Node(key, value)
        # add it to the right as the most recent
        self.insert(self.cache[key])

        # if it exceeds the capacity, we remove the least recent used, which is at the left
        if len(self.cache) > self.cap:
            lru = self.left.next
            # remove it from the linked list
            self.remove(lru)
            # delete it from the cache
            del self.cache[lru.key]