class Solution:
    def maxPoints(self, grid, queries):
        """
        :type grid: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Directions for movement
        
        # Union-Find (Disjoint Set Union) helpers
        parent = {}
        size = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if size[rootX] < size[rootY]:
                    rootX, rootY = rootY, rootX
                parent[rootY] = rootX
                size[rootX] += size[rootY]
        
        # Flatten the grid and sort cells by value
        cells = sorted([(grid[i][j], i, j) for i in range(m) for j in range(n)])
        queries_with_idx = sorted([(q, i) for i, q in enumerate(queries)])
        
        visited = [[False] * n for _ in range(m)]  # To track visited cells
        result = [0] * len(queries)  # To store the results for each query
        index = 0  # To iterate over sorted grid cells
        points = 0  # To track the number of points
        
        # Process each query
        for query_val, query_idx in queries_with_idx:
            # Explore all cells whose value is smaller than the current query value
            while index < len(cells) and cells[index][0] < query_val:
                val, x, y = cells[index]
                index += 1
                if visited[x][y]:
                    continue
                visited[x][y] = True
                parent[(x, y)] = (x, y)
                size[(x, y)] = 1
                points += 1
                
                # Union the current cell with its neighbors (if they are already visited)
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and visited[nx][ny]:
                        union((x, y), (nx, ny))
            
            # For the current query, find the connected component size of (0, 0)
            if visited[0][0]:
                result[query_idx] = size[find((0, 0))]
            else:
                result[query_idx] = 0
        
        return result

# Example 1
grid1 = [[1, 2, 3], [2, 5, 7], [3, 5, 1]]
queries1 = [5, 6, 2]
print(Solution().maxPoints(grid1, queries1))  # Output: [5, 8, 1]

# Example 2
grid2 = [[5, 2, 1], [1, 1, 2]]
queries2 = [3]
print(Solution().maxPoints(grid2, queries2))  # Output: [0]
