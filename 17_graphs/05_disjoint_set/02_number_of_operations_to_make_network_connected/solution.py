# https://leetcode.com/problems/number-of-operations-to-make-network-connected/
from typing import *

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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # If we have fewer than n-1 connections, it's impossible to connect all computers
        if len(connections) < n - 1:
            return -1
        
        # Initialize DisjointSet (note: computers are numbered 0 to n-1)
        ds = DisjointSet(n)
        
        # Count extra cables (redundant connections)
        extra_edges = 0
        
        # Process all connections
        for a, b in connections:
            # If a and b are already in the same component, this is a redundant edge
            if ds.findUltimateParent(a) == ds.findUltimateParent(b):
                extra_edges += 1
            else:
                # Otherwise, union the components
                ds.unionByRank(a, b)
        
        # Count the number of connected components
        components = set()
        for i in range(n):
            components.add(ds.findUltimateParent(i))
        
        # Number of connected components
        num_components = len(components)
        
        # We need (num_components - 1) operations to connect all components
        required_ops = num_components - 1
        
        # Check if we have enough extra edges
        return required_ops