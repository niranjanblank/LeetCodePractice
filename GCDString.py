import math

# solution1
def gcdOfStrings1(str1: str, str2: str) -> str:
    min_length = min(len(str1), len(str2))
    for i in range(min_length,0,-1):
        if min_length % i == 0 :
            potential_gcd = str1[0:i]
            gcd_str1 = potential_gcd*(len(str1)//i)
            gcd_str2 = potential_gcd*(len(str2)//i)
            if (gcd_str1 == str1) and (gcd_str2 == str2):
                return potential_gcd
    return ""

def gcdOfStrings(str1: str, str2: str) -> str:
    if (str1+str2) != (str2+str1):
        return ""

    gcd_length = math.gcd(len(str1), len(str2))

    return str1[:gcd_length]

print(gcdOfStrings("ABABAB","ABAB"))