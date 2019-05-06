def isBoomerang(points):
    points.sort(key=lambda x: x[0])
    if points[2] == points[1] or points[1] == points[0] or points[0] == points[2]:
        return False
    if (points[2][0] == points[1][0] and points[1][0] == points[0][0]) or (points[2][1] == points[1][1] and points[1][1] == points[0][1]):
        return False
    if points[1][0] - points[0][0] == points[2][0] - points[1][0] and points[1][1] - points[0][1] == points[2][1] - points[1][1]:
        return False
    
    return True
    




print(isBoomerang(points=[[2,3],[3,2],[1,1]]))
print(isBoomerang(points=[[1,1],[2,2],[3,3]]))
print(isBoomerang(points=[[0,0],[1,1],[1,1]]))
print(isBoomerang(points=[[0,0],[0,2],[2,1]]))
