# https://leetcode.com/problems/course-schedule/
# Solved this problem using topological sort.. BFS.. Kahn's algo
from typing import *
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses

        # create adjList
        adjList = [[] for _ in range(numCourses)]

        for requisite in prerequisites:
            v, u = requisite
            adjList[u].append(v)

        # create indegree array
        for requisite in prerequisites:
            v, u = requisite
            indegree[v] += 1

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        course_order = []

        while queue:
            curr = queue.popleft()
            course_order.append(curr)

            for next_node in adjList[curr]:
                indegree[next_node] -= 1

                if indegree[next_node] == 0:
                    queue.append(next_node)

        if len(course_order) == numCourses:
            return True
        
        return False