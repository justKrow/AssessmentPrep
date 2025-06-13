# Easy Array Problem: “Merge Sorted Arrays”
# 🧩 Prompt:
# You are given two sorted integer arrays nums1 and nums2, and an integer m and n representing the number of elements in nums1 and nums2 respectively.

# Merge nums2 into nums1 as one sorted array in-place.
# You can assume nums1 has enough space to hold the result (size of nums1 is m + n).
# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3

def mergedSortedArray(nums1, nums2, m , n):
    i = m -1  # last index of nums1 of real val
    j = n - 1 # last index of nums2 of real val
    k = m + n - 1 # last index of nums1

    while i >= 0 and j >= 0:
        if nums2[j] > nums1[i]:
            nums1[k] = nums2[j]
            j -= 1
        else:
            nums1[k] = nums1[i]
            i -= 1
        k -=1

    while j >= 0:
        nums1[k] = nums2[j]
        j-=1
        k-=1
    return nums1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

mergedSortedArray(nums1, nums2,m, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
