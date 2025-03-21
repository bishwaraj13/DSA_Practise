# https://leetcode.com/problems/number-of-islands-ii/
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * (n)
        self.size = [1] * (n)
    
    def findUltimateParent(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.findUltimateParent(self.parent[x])
        return self.parent[x]
    
    def unionByRank(self, x, z):
        x_root = self.findUltimateParent(x)
        z_root = self.findUltimateParent(z)
        
        if x_root == z_root:
            return
        
        if self.rank[x_root] < self.rank[z_root]:
            self.parent[x_root] = z_root
        elif self.rank[x_root] > self.rank[z_root]:
            self.parent[z_root] = x_root
        else:
            self.parent[x_root] = z_root
            self.rank[z_root] += 1

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        node_count = m * n
        ds = DisjointSet(node_count)
        visited = [[0 for j in range(n)] for i in range(m)]
        result = []

        countComponents = 0
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        for r, c in positions:
            node = r * n + c
            if visited[r][c]:
                result.append(countComponents)
                continue
            visited[r][c] = 1
            # increase the component count
            countComponents += 1

            for dr, dc in directions:
                adj_r = r + dr
                adj_c = c + dc

                if 0 <= adj_r < m and 0 <= adj_c < n and visited[adj_r][adj_c]:
                    adj_node = adj_r * n + adj_c
                    if ds.findUltimateParent(node) != ds.findUltimateParent(adj_node):
                        # if they have different parent, they have to be connected
                        # and componentCount should decrease by 1
                        ds.unionByRank(node, adj_node)
                        countComponents -= 1

            result.append(countComponents)
                 
        return result
