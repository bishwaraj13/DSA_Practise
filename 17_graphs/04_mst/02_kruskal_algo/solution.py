from typing import List

##### Code for MST (kruskal) is below Disjoint Set class
##### We use Disjoint Set as data structure in Kruskal

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)
        self.size = [1] * (n+1)
    
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
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        # Extract edges from adjacency list
        # O(N + E)
        edges = []
        for u in range(V):
            for v, w in adj[u]:
                # Add edge only once (when u < v to avoid duplicates)
                if u < v:
                    edges.append((u, v, w))
        
        # Sort edges by weight
        # O (M log M)
        edges.sort(key=lambda x: x[2])
        
        # Create DisjointSet
        ds = DisjointSet(V-1)  # V-1 because 0-indexed
        
        mst_weight = 0
        mst_edges = 0
        
        # Process edges in ascending order of weight
        # O (M x 4 x alpha) x 2
        for u, v, w in edges:
            # If including this edge doesn't form a cycle
            if ds.findUltimateParent(u) != ds.findUltimateParent(v):
                # Add edge to MST
                mst_weight += w
                ds.unionByRank(u, v)
                mst_edges += 1
                
                # Early termination: MST will have V-1 edges
                if mst_edges == V-1:
                    break
        
        return mst_weight