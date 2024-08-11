# You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.

# The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

# In one day, we are allowed to change any single land cell (1) into a water cell (0).

# Return the minimum number of days to disconnect the grid.

 

# Example 1:


# Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]

# Output: 2
# Explanation: We need at least 2 days to get a disconnected grid.
# Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
# Example 2:


# Input: grid = [[1,1]]
# Output: 2
# Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 30
# grid[i][j] is either 0 or 1.

class Solution:
  def minDays(self, grid: list[list[int]]) -> int:
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    m = len(grid)
    n = len(grid[0])

    def dfs(grid: list[list[int]], i: int, j: int, seen: set[tuple[int, int]]):
      seen.add((i, j))
      for dx, dy in dirs:
        x = i + dx
        y = j + dy
        if x < 0 or x == m or y < 0 or y == n:
          continue
        if grid[x][y] == 0 or (x, y) in seen:
          continue
        dfs(grid, x, y, seen)

    def disconnected(grid: list[list[int]]) -> bool:
      islandsCount = 0
      seen = set()
      for i in range(m):
        for j in range(n):
          if grid[i][j] == 0 or (i, j) in seen:
            continue
          if islandsCount > 1:
            return True
          islandsCount += 1
          dfs(grid, i, j, seen)
      return islandsCount != 1

    if disconnected(grid):
      return 0

    # Try to remove 1 land.
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1:
          grid[i][j] = 0
          if disconnected(grid):
            return 1
          grid[i][j] = 1

    # Remove 2 lands.
    return 2