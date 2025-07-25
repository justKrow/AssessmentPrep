# Problem: Number of Islands(Leetcode  # 200)
# 🔍 Prompt:
# You are given a 2D grid of '1' (land) and '0' (water).
# Return the number of islands — where an island is a group of connected '1's horizontally or vertically.
# grid = [
#     ["1", "1", "0", "0"],
#     ["1", "0", "0", "1"],
#     ["0", "0", "1", "1"]
# ]


def numberOfIslands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
            return
        grid[r][c] = "0"
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1":
                count += 1
                dfs(row, col)
    return count


print(numberOfIslands([
    ["1", "1", "0", "0"],
    ["1", "0", "0", "1"],
    ["0", "0", "1", "1"]
]))
