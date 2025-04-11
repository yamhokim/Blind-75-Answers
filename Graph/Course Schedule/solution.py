class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = []

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        unvisited = 0
        visiting = 1
        visited = 2

        states = [unvisited] * numCourses

        def dfs(node):
            state = states[node]
            if state == visited:
                return True
            elif state == visiting:
                return False
            
            states[node] = visiting
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            states[node] = visited
            return True

        for num in range(numCourses):
            if not dfs(num):
                return False

        return True