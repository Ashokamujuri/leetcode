class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k = k % total  # Normalize k if it's larger than the total number of elements
        flat = [grid[r][c] for r in range(m) for c in range(n)]
        shifted = flat[-k:] + flat[:-k]
        ans = []
        for i in range(m):
            ans.append(shifted[i * n : (i + 1) * n])

        return ans