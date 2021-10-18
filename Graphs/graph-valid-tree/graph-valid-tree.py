from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        adj_list = defaultdict(list)
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)
        
        visited = set()
        def dfs(node):
            if node in visited: return
            visited.add(node)
            for neighbor in adj_list[node]:
                dfs(neighbor)
         
        dfs(0)
        return len(visited) == n