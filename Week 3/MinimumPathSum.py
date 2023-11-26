#Medium
#Matrix
# Approach 1: Brute Force
# Recursion - for each elem, consider 2 paths - right and down - find min sum out of the two
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def calculate(grid, i, j):
            if i == len(grid) or j == len(grid[0]):
                return float('inf')
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return grid[i][j]
            return grid[i][j] + min(calculate(grid, i + 1, j), calculate(grid, i, j + 1))

        return calculate(grid, 0, 0)

#Time: O(2^(m+n))
#Space: O(m + n)

# Approach 2: Dynamic Programming 2D
class Solution:
    def minPathSum(self, grid):
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(rows)]

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i == rows - 1 and j != cols - 1:
                    dp[i][j] = grid[i][j] + dp[i][j + 1]
                elif j == cols - 1 and i != rows - 1:
                    dp[i][j] = grid[i][j] + dp[i + 1][j]
                elif j != cols - 1 and i != rows - 1:
                    dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])
                else:
                    dp[i][j] = grid[i][j]

        return dp[0][0]

#Time: O(mn)
#Space: O(mn)