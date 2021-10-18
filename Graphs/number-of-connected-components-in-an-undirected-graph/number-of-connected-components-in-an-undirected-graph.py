class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
            
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for children in adj_list[node]:
                dfs(children) 
            return True
            
        connected_components = 0
        for i in range(n):
            if i not in visited:
                connected_components += 1
                dfs(i)
        return connected_components
            