# ✅ Problem: Insert Interval
# 🔍 Prompt:
# You are given a list of non-overlapping intervals sorted by their start time, and a new interval to insert.

# Insert the new interval into the list, merging if necessary to maintain non-overlapping order.
# intervals = [[1,3],[6,9]]
# newInterval = [2,5]

def insertInterval(intervals, new_interval):
    if not intervals:
        return []
    # merged_intervals = []
    # for interval in intervals:
    #     if len(merged_intervals) == 0:
    #         merged_intervals.append(interval)
    #     if new_interval[0] < merged_intervals[-1][1] and new_interval[0] > merged_intervals[-1][0]:
    #         print("here")
    #         merged_intervals[-1] = [
    #             merged_intervals[-1][0],
    #             max(new_interval[1], merged_intervals[-1][1])]
    #     elif new_interval[0] > merged_intervals[-1][1] and new_interval[1] < interval[0]:
    #         merged_intervals.append(new_interval)
    #     if interval[0] < merged_intervals[-1][1]:
    #         merged_intervals[-1] = [merged_intervals[-1][0], max(
    #             merged_intervals[-1][1], interval[1])]
    #     elif interval[0] > merged_intervals[-1][1]:
    #         merged_intervals.append(interval)
    # return merged_intervals
    i = 0
    merged_intervals = []
    n = len(intervals)
    while i < n and intervals[i][1] < new_interval[0]:
        merged_intervals.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(intervals[i][0], new_interval[0])
        new_interval[1] = max(intervals[i][1], new_interval[1])
        i += 1
    merged_intervals.append(new_interval)

    while i < n:
        merged_intervals.append(intervals[i])
        i += 1
    return merged_intervals


print(insertInterval([[1, 3], [6, 9]], [2, 5]))
