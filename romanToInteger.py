def romanToInt(s):
    # going from back to front
    map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    s = s[::-1]
    curr_num = map[s[0]]
    for i in range(1,len(s)):
        if curr_num <= map[s[i]] or map[s[i]] == map[s[i-1]]:
            curr_num += map[s[i]]
        else:
            curr_num = curr_num - map[s[i]]

    return curr_num

def romanToInt2(s):
    # larger to smaller add
    # smaller to larger subtract
    map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    res = 0
    for i in range(len(s)):
        if i + 1 < len(s) and map[s[i]]<map[s[i+1]]:
            res -= map[s[i]]
        else:
            res += map[s[i]]
    return res



