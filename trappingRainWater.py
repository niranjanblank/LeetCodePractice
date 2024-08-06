"""
42. Trapping Rain Water
Hard
Topics
Companies
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

# solution
# with O(n) memory
# min(L,R) - h[i]
def trap(height):
    left=[0]*len(height)
    right=[0]*len(height)
    # calculating the max_value from left to current value
    max_till_now = 0
    for i in range(len(height)):
        max_till_now=max(max_till_now,height[i])
        left[i] = max_till_now

    # for right
    max_till_now = 0
    for i in range(len(height)-1,-1,-1):
        max_till_now = max(max_till_now, height[i])
        right[i] = max_till_now

    min_left_right = []

    for i in range(len(height)):
        min_left_right.append(min(left[i],right[i]))

    total_water_trapped = 0
    for i in range(len(height)):
        water = min_left_right[i] - height[i]
        if water < 0:
            water = 0
        total_water_trapped += water
    return(total_water_trapped)


# solution 2
# O(1) space complexity
# two pointers solution
def trap_two_pointer(height):
    if not height: return 0

    l,r = 0, len(height)-1
    max_left, max_right = height[l],height[r]
    result = 0

    while l<r:
        if max_left < max_right:
            l+=1
            max_left = max(max_left, height[l])
            result += max_left - height[l]
        else:
            r -= 1
            max_right = max(max_right, height[r])
            result += max_right - height[r]

    return result



print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap_two_pointer([0,1,0,2,1,0,1,3,2,1,2,1]))