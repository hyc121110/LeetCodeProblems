def dfs(graph, start, visited=None):
  if visited is None:
    visited = set()
  visited.add(start)
  for next in graph[start] - visited:
    dfs(graph, next, visited)
  return visited

def dfs_paths(graph, start, goal):
  stack = [(start, [start])]
  while stack:
    (vertex, path) = stack.pop()
    for next in graph[vertex] - set(path):
      if next == goal:
        yield path + [next]
      else:
        stack.append((next, path + [next]))