def kidsWithCandies(candies, extraCandies):
    result = [True]*5

    for i in range(len(candies)):
        if (candies[i] + extraCandies) < max(candies):
            result[i] = False
    return result

print(kidsWithCandies([2,3,5,1,3],3))