'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
'''

def canFinish(numCourses, prerequisites):
  def dfs(graph, visited, i):
    # if ith node is marked as being visited, then a cycle is found
    if visited[i] == -1:
      return False
    # if it is done visted, then do not visit again
    elif visited[i] == 1:
      return True
    # else: mark as being visited
    visited[i] = -1
    # visit all the neighbours
    for j in graph[i]:
      if not dfs(graph, visited, j):
        return False
    # after visit all the neighbours, mark it as done visited
    visited[i] = 1
    return True

  # if the graph has a cycle -> return false
  graph = [[] for _ in range(numCourses)]
  visited = [0] * numCourses

  # create graph
  for pair in prerequisites:
    x, y = pair
    graph[x].append(y)

  # visit each node
  for i in range(numCourses):
    if not dfs(graph, visited, i):
      return False
  return True

numCourses = 2
prerequisites = [[1,0],[0,1]]
print(canFinish(numCourses, prerequisites))