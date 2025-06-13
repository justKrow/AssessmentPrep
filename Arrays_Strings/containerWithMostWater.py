# Problem: "Container With Most Water"
# Prompt:
# You are given an array height of length n. Each element represents the height of a vertical line at that index. The goal is to find two lines that, together with the x-axis, form a container that can store the most water.

height = [1,8,6,2,5,4,8,3,7]
expected_output = 49

def findLargestArea(height):
    left_wall = 0
    right_wall = len(height) - 1
    max_area = 0
    while right_wall > left_wall:
        width = right_wall - left_wall
        min_height = min(height[left_wall], height[right_wall])
        area = width * min_height
        max_area = max(max_area, area)
        if height[left_wall] < height[right_wall]:
            left_wall += 1
        else:
            right_wall-=1
    return max_area

print(findLargestArea(height))