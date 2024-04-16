def canFinish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    visited = [0] * numCourses  # 0: unvisited, 1: visiting, -1: visited

    def dfs(course):
        if visited[course] == 1:
            return False
        if visited[course] == -1:
            return True
        visited[course] = 1
        for next_course in graph[course]:
            if not dfs(next_course):
                return False
        visited[course] = -1
        return True

    for dest, src in prerequisites:
        graph[src].append(dest)

    for course in range(numCourses):
        if visited[course] == 0:
            if not dfs(course):
                return False
    return True

# Testing the function
print(canFinish(2, [[1, 0]]))  # True
print(canFinish(2, [[1, 0], [0, 1]]))  # False
