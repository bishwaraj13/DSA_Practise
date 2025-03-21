# https://leetcode.com/problems/making-a-large-island/
from typing import *

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * (n)
    
    def findUltimateParent(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.findUltimateParent(self.parent[x])
        return self.parent[x]

    def unionBySize(self, x, z):
        x_root = self.findUltimateParent(x)
        z_root = self.findUltimateParent(z)

        if x_root == z_root:
            return
        
        if self.size[x_root] < self.size[z_root]:
            self.parent[x_root] = z_root
            self.size[z_root] += self.size[x_root]
        else:
            self.parent[z_root] = x_root
            self.size[x_root] += self.size[z_root]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        node_count = m * n

        ds = DisjointSet(node_count)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for r in range(m):
            for c in range(n):
                node_num = r * n + c

                if grid[r][c] != 1:
                    continue

                for dr, dc in directions:
                    adj_r = r + dr
                    adj_c = c + dc

                    adj_node_num = adj_r * n + adj_c

                    if (0 <= adj_r < m and 0 <= adj_c < n and grid[adj_r][adj_c]):
                        ds.unionBySize(node_num, adj_node_num)

        # Find maximum island size
        max_size = 0
        for i in range(node_count):
            max_size = max(max_size, ds.size[ds.findUltimateParent(i)])

        # Try converting each water cell to land
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    continue
                    
                node_num = r * n + c
                
                # Track visited parent nodes to avoid double counting
                visited_parents = set()
                size_after_conversion = 1  # Start with 1 for the converted cell
                
                for dr, dc in directions:
                    adj_r = r + dr
                    adj_c = c + dc
                    
                    if 0 <= adj_r < m and 0 <= adj_c < n and grid[adj_r][adj_c] == 1:
                        adj_node_num = adj_r * n + adj_c
                        parent = ds.findUltimateParent(adj_node_num)
                        
                        if parent not in visited_parents:
                            visited_parents.add(parent)
                            size_after_conversion += ds.size[parent]
                
                max_size = max(max_size, size_after_conversion)

        return max_size
                