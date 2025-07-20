# ✅ First Problem: Merge Intervals
# 🔍 Problem Statement:
# Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.
# 🔸 Example:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

def mergeIntervals(intervals):
    merged_intervals = []
    intervals.sort(key=lambda x: x[0])
    for interval in intervals:
        if len(merged_intervals) == 0:
            merged_intervals.append(interval)
        if interval[0] < merged_intervals[-1][1]:
            merged_intervals[-1] = [merged_intervals[-1][0],
                                    max(interval[1], merged_intervals[-1][1])]
        if interval[0] > merged_intervals[-1][1]:
            merged_intervals.append(interval)
    return merged_intervals


print(mergeIntervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
