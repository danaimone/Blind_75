from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        '''
            Intuition:
            Go through the matrix, searching for a node of land.
            When you find land, perform a depth-first-search on that node.
            After performing the depth-first search, mark the node as 0 as a way of
            keeping a "visited" for dfs, since we don't want to revisit islands.
            If we're out of bounds, we also want to get out of our recursive loop. Otherwise,
            perform a DFS on the north, south, west, and east neighbors, marking all the valid land cells
            as water on the way. Once we break out of DFS, we will have covered one island, and can
            move forward through the array, upping a counter after each complete return from DFS.

            Time Complexity:
            O(row * col)

            Space Complexity:
            O(row * col), in worst case our recursion stack could be called on a grid full of land.

        :param grid:
        :return:
        '''
        def dfs(i, j, grid):
            num_rows = len(grid)
            num_cols = len(grid[0])
            if i < 0 or j < 0 or i >= num_rows or j >= num_cols: # we're out of bounds!
                return

            if grid[i][j] == "0":  # we've hit water, no longer on an island
                return

            grid[i][j] = "0" # setting it so we don't revisit in a cycle

            dfs(i, j + 1, grid)
            dfs(i, j - 1, grid)
            dfs(i - 1, j, grid)
            dfs(i + 1, j, grid)

        if grid is None or len(grid) == 0:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":  # found land, let's dfs through and see how far this goes out
                   count += 1
                   dfs(i, j, grid)
        return count
