def reverseVowels(s):
    vowels = "aeiouAEIOU"
    s = list(s)
    i = 0
    j = len(s)-1


    while i<j:
        if s[i] not in vowels:
            i+=1
            continue
        if s[j] not in vowels:
            j-=1
            continue

        # swap if both letters are vowels
        s[i], s[j] = s[j], s[i]
        i+=1
        j-=1
    return ''.join(s)

print(reverseVowels('hello'))