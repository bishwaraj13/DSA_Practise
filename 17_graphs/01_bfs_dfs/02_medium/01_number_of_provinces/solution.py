# https://leetcode.com/problems/number-of-provinces/
from typing import *

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node, adjList, visited):
            visited[node] = 1

            for neighbour in adjList[node]:
                if not visited[neighbour]:
                    dfs(neighbour, adjList, visited)

            return

        V = len(isConnected)

        # create adjacencey list
        adjList = [[] for _ in range(V)]

        for i in range(V):
            for j in range(V):
                # self nodes are not considered
                if i != j and isConnected[i][j] == 1:
                    adjList[i].append(j)
                    adjList[j].append(i)

        
        # create visited list
        visited = [0] * V
        count = 0

        for i in range(V):
            if not visited[i]:
                count += 1
                dfs(i, adjList, visited)

        return count
            
