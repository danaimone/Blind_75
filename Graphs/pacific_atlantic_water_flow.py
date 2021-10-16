from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        num_rows, num_cols = len(heights), len(heights[0])

        pacific_queue = deque()
        atlantic_queue = deque()

        for i in range(num_rows):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, num_cols - 1))

        for j in range(num_cols):
            pacific_queue.append((0, j))
            atlantic_queue.append((num_rows - 1, j))

        def bfs(queue):
            reachable = set()
            while queue:
                (row, col) = queue.popleft()
                reachable.add((row, col))
                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for (x, y) in directions:
                    new_row, new_col = row + x, col + y
                    if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                        continue

                    if (new_row, new_col) in reachable:
                        continue

                    smaller_height = heights[new_row][new_col] < heights[row][col]
                    if smaller_height:
                        continue

                    queue.append((new_row, new_col))
            return reachable

        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)

        return list(pacific_reachable.intersection(atlantic_reachable))