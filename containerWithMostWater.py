def maxArea(height):
    start_index = 0
    end_index = len(height)-1
    max_area = 0
    while start_index<end_index:
        width = end_index - start_index
        min_height = min(height[start_index], height[end_index])
        area = min_height * width
        if area > max_area:
            max_area = area

        if height[start_index] < height[end_index]:
            start_index += 1
        else:
            end_index -= 1

    return max_area


def max_area(height):
    left = 0
    right = len(height)-1
    maxi_area = 0
    while left < right:
        width = right - left
        min_height = min(height[left], height[right])
        area = width * min_height

        maxi_area = max(area, maxi_area)

        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

    return maxi_area

def max_area_2(height):
    left = 0
    right = len(height)-1
    maxi_area = 0

    while left < right:
        maxi_area = max(maxi_area, min(height[left], height[right])* (right-left))
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return maxi_area

print(maxArea([1,4,2,3]))
print(maxArea([1,8,6,2,5,4,8,3,7]))