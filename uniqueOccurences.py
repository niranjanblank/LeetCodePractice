def uniqueOccurences(arr):
    hash_table = {}
    for item in arr:
        hash_table[item] = hash_table.get(item,0) + 1
    return len(set(hash_table.values())) == len(hash_table.values())
print(uniqueOccurences([-3,0,1,-3,1,1,1,-3,10,0]))


