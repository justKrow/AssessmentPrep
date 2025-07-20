# ✅ Problem: Minimum Number of Arrows to Burst Balloons
# 🔍 Prompt:
# You are given a list of balloons, where each balloon is represented by a 2D interval[start, end] — the x-coordinates of its horizontal diameter.

# You need to burst all balloons using the minimum number of arrows.
# An arrow can be shot vertically, and it bursts all balloons that it touches(i.e., overlaps).

def minimumArrows(points):
    points.sort(key=lambda x: x[1])
    arrow_count = 1
    i = 0
    arrow_end = points[0][1]

    for start, end in points[1:]:
        if start > arrow_end:
            arrow_count += 1
            arrow_end = end
    return arrow_count


print(minimumArrows([[10, 16], [2, 8], [1, 6], [7, 12]]))
