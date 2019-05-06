'''
We are given a matrix with R rows and C columns has cells with integer coordinates (r, c), where 0 <= r < R and 0 <= c < C.

Additionally, we are given a cell in that matrix with coordinates (r0, c0).

Return the coordinates of all cells in the matrix, sorted by their distance from (r0, c0) from smallest distance to largest distance.  Here, the distance between two cells (r1, c1) and (r2, c2) is the Manhattan distance, |r1 - r2| + |c1 - c2|.  (You may return the answer in any order that satisfies this condition.)
'''

def allCellsDistOrder(R, C, r0, c0):
    # method 1: dfs (slow)
    # def dfs(i, j):
    #     seen.add((i, j))
    #     res.append([i, j])
    #     for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
    #         if 0 <= x < R and 0 <= y < C and (x, y) not in seen:
    #             dfs(x, y)
    # res, seen = [], set()
    # dfs(r0, c0)
    # return sorted(res, key = lambda x: abs(x[0] - r0) + abs(x[1] - c0))

    # method 2: 
    # res = [[r0, c0]]
    # for d in range(1, R+C-1):
    #     for x in range(d, -d-1, -1):
    #         r1 = r0 + x; c1 = c0 + d - abs(x); c2 = c0 + abs(x) - d
    #         if 0 <= r1 < R:
    #             if 0 <= c1 < C: res.append([r1,c1])
    #             if c1 != c2 and 0 <= c2 < C: res.append([r1,c2])
    # return res

    # method 3:
    def dists(points):
        pi, pj = points
        return abs(pi - r0) + abs(pj - c0)
    
    points = [(i, j) for i in range(R) for j in range(C)]
    
    return sorted(points, key = dists)
    
R=2
C=3
r0=0
c0=0
print(allCellsDistOrder(R,C,r0,c0))