'''
A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.
'''

# idea: if the three points cannot form a triangle, it is not a boomerang
def isBoomerang(points):
    # stupid solution
    # points.sort(key=lambda x: x[0])
    # if points[2] == points[1] or points[1] == points[0] or points[0] == points[2]:
    #     return False
    # if (points[2][0] == points[1][0] and points[1][0] == points[0][0]) or (points[2][1] == points[1][1] and points[1][1] == points[0][1]):
    #     return False
    # if points[1][0] - points[0][0] == points[2][0] - points[1][0] and points[1][1] - points[0][1] == points[2][1] - points[1][1]:
    #     return False
    
    # return True
    
    # smarter solution: calculate slopes
    '''
    -assume the slope of the line using points 0 and 1 (a/b) and that of using points 0  and 2 (c / d)
    -avoid dividing, just compare a/b and c/d if(a * d > c * b)==> first fraction is greater otherwise second
    -if slopes of the both lines (p0--p1 and p0--p2) are equal then three points form a straight line (cannot form a triangle)
    '''
    return (points[1][1] - points[0][1]) * (points[2][0] - points[0][0]) != (points[2][1] - points[0][1]) * (points[1][0] - points[0][0])

print(isBoomerang(points=[[2,3],[3,2],[1,1]]))
print(isBoomerang(points=[[1,1],[2,2],[3,3]]))
print(isBoomerang(points=[[0,0],[1,1],[1,1]]))
print(isBoomerang(points=[[0,0],[0,2],[2,1]]))
