'''
You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.

paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.

Also, there is no garden that has more than 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.  The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.
'''

# Greedily paint nodes one by one.
# Because there is no node that has more than 3 neighbors,
# always one possible color to choose.

def gardenNoAdj(N, paths):
  res = [0] * N
  G = [[] for i in range(N)]
  for x, y in paths:
    G[x - 1].append(y - 1)
    G[y - 1].append(x - 1)
  for i in range(N):
    temp = {1, 2, 3, 4} - {res[j] for j in G[i]}
    res[i] = temp.pop()
  return res

print(gardenNoAdj(N=4, paths=[[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]))
print(gardenNoAdj(N=4, paths=[[1,2],[3,4]]))
print(gardenNoAdj(N=4, paths=[[1,2],[2,3],[3,1]]))
print(gardenNoAdj(N=5, paths=[[1,2],[2,3],[3,4],[4,5],[1,5]]))
