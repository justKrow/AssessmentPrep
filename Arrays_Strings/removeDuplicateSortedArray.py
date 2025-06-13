# Easy array/pointer: “Remove Duplicates from Sorted Array”

def removeDuplicate(arr):
    if not arr:
        return []
    j = 0
    for i in range(1, len(arr)):
        if arr[j] != arr[i]:
            j += 1
            arr[j] = arr[i]
    return arr[:j+1]

print(removeDuplicate([1,2,2,3,5,8,8,10]))