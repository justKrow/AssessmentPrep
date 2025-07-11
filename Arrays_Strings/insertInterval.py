# You are given a list of non-overlapping intervals sorted by their start times.
# You are also given a new interval, and you need to insert it into the list while preserving the order and merging if necessary.
# intervals = [[1, 3], [6, 9]]
# new_interval = [2, 5]
# Output: [[1,5],[6,9]]

def insertInterval(intervals, new_interval):
    result = []
    i = 0
    n = len(intervals)

    # 1. Add all intervals before the new_interval
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # 2. Merge overlapping intervals with new_interval
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    result.append(new_interval)

    # 3. Add the rest of the intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result


print(insertInterval([[1, 3], [6, 9]], [2, 5]))
