"""
Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of same
length with the squares of the original integers also sorted in ascending order
"""

# For Ascending order
def sortedSquaredArray(array):
    left = 0
    right = len(array) - 1

    results = [0]*len(array)

    for i in range(len(array)-1, -1, -1):
        if abs(array[left]) > abs(array[right]):
            results[i] = array[left] ** 2
            left += 1
        else:
            results[i] = array[right] ** 2
            right -=1
    return results


# For Descending order
def sortedSquaredArrayDesc(array):
    left = 0
    right = len(array) - 1
    results = [0]*len(array)

    for i in range(0, len(array)-1):
        if abs(array[left]) > abs(array[right]):
            results[i] = array[left] ** 2
            left += 1
        else:
            results[i] = array[right] ** 2
            right -= 1
    return results

print(sortedSquaredArray([-4, -1, 0, 3, 10]))
print(sortedSquaredArrayDesc([-4, -1, 0, 3, 10]))