"""
Leetcode 207: Course Schedule

Problem Description:
You are given a number of courses, each with prerequisites, and you need to determine if it's possible to finish all the courses. Each course may have prerequisites, represented as a directed graph where an edge from course `a` to course `b` means that course `a` is a prerequisite for course `b`. The problem asks if it's possible to complete all courses without encountering a cycle. If a cycle exists in the graph, it would be impossible to finish the courses. The solution must return `True` if it's possible to finish all courses, and `False` otherwise.

Approach:
1. **Topological Sorting Using Kahn’s Algorithm**: This approach uses a graph and in-degree of each node (course). We perform a BFS starting from courses with no prerequisites and reduce the in-degree of other courses as we complete each course.
2. **Check for Cycles**: If, after processing all courses, there are still courses with non-zero in-degree, it means there is a cycle, and completing all courses is impossible.
3. **Return True or False**: If all courses are processed successfully, return `True`. If a cycle is detected, return `False`.
"""

from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Create an adjacency list and in-degree array
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        # Step 2: Build the graph and in-degree array
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1

        # Step 3: Initialize queue with courses having in-degree 0
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        # Step 4: Process courses using BFS
        completed_courses = 0

        while queue:
            course = queue.popleft()
            completed_courses += 1

            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 5: Check if all courses were completed
        return completed_courses == numCourses

# Example usage
solution = Solution()
print(solution.canFinish(2, [[1,0]]))       # Output: True
print(solution.canFinish(2, [[1,0],[0,1]])) # Output: False

