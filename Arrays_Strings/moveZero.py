# Given an integer array nums, move all 0's to the end while maintaining the relative order of the non-zero elements.
# You must do this in-place without making a copy of the array.
# Input:  [0, 1, 0, 3, 12]  
# Output: [1, 3, 12, 0, 0]

def moveZero(arr):
    last_non_zero = 0
    for i in range(len(arr)):
        if arr[i]!= 0:
            arr[i], arr[last_non_zero] = arr[last_non_zero], arr[i]
            last_non_zero+=1
    return arr

print(moveZero([0, 1, 0, 3, 12]))