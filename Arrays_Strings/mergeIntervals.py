# Given an array of intervals where intervals[i] = [start, end],
# merge all overlapping intervals and return an array of the non-overlapping intervals.
# Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# Output: [[1, 6], [8, 10], [15, 18]]
# Explanation:

# [1,3] and [2,6] overlap → merge to [1,6]

# [8,10] and [15,18] don’t overlap


def mergeInterval(intervals):
    # intervals = sorted(intervals)
    # merged = []
    # for interval in intervals:
    #     if not merged or merged[-1][1] < interval[0]:
    #         merged.append(interval)
    #     else:
    #         merged[-1][1] = max(merged[-1][1], interval[1])
    # return merged
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    output = [intervals[0]]
    for interval in intervals[1:]:
        last = output[-1]
        if last[1] >= interval[0]:
            last[1] = max(last[1], interval[1])
        else:
            output.append(interval)
    return output


print(mergeInterval([[1, 3], [2, 6], [8, 10], [15, 18]]))
