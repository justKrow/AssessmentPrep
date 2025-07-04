# Problem: “Merge Intervals”
# Prompt:
# Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example:
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Intervals [1,3] and [2,6] overlap, so they are merged into [1,6].

def mergeIntervals(intervals):
    if not intervals:
        return []

    # Step 1: Sort intervals by the start time
    intervals.sort(key=lambda x: x[0])
    output = [intervals[0]]

    for current in intervals[1:]:
        last = output[-1]

        # If there's overlap, merge
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            output.append(current)

    return output


# Test
print(mergeIntervals([[1, 3], [2, 6], [8, 10], [11, 18]]))
