#  BFS Approach (Optimal, Clean, Interviewable)
# This is multi-source BFS:

# Think of all initial rotten oranges as level 0 of BFS

# In each minute, rot adjacent fresh ones → they go to next level

# Continue until there are no fresh oranges left
# grid = [
#   [2, 1, 1],
#   [1, 1, 0],
#   [0, 1, 1]
# ]

from collections import deque


def rottingOranges(grid):
    rows = len(grid)
    cols = len(grid[0])
    queue = deque()
    fresh_oranges = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh_oranges += 1

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    time = 0
    while queue:
        r, c, minute = queue.popleft()
        time = max(time, minute)
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh_oranges -= 1
                queue.append((nr, nc, minute + 1))
    return time if fresh_oranges == 0 else -1


print(rottingOranges([
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]))
