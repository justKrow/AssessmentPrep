# ✅ Problem: Non-overlapping Intervals
# 🔍 Prompt:
# Given an array of intervals where intervals[i] = [start_i, end_i], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1

# Explanation:
# Remove [1,3] to get non-overlapping intervals [[1,2],[2,3],[3,4]]

def nonOverlappingIntervals(intervals):
    if not intervals:
        return []
    count = 0
    intervals.sort(key=lambda x: x[1])
    print(intervals)
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            count += 1
        else:
            end = intervals[i][1]
    return count


print(nonOverlappingIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
