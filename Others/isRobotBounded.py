'''
On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
'''

# only consider the final position:
# 1. if facing north from (0, 0) to (x, y), it will continue to face north
# 2. if face other direction, it will return to origin position
def isRobotBounded(instructions):
  x, y, dx, dy = 0, 0, 0, 1
  for i in instructions:
    # (0,1) -> (1,0) -> (0, -1) -> (-1, 0)
    if i == 'R': dx, dy = dy, -dx
    # opposite of above
    if i == 'L': dx, dy = -dy, dx
    # next position
    if i == 'G': x, y = x + dx, y + dy
  # return true if either return to orig position or not facing north
  return (x, y) == (0, 0) or (dx, dy) != (0,1)

print(isRobotBounded(instructions="GGLLGG"))
print(isRobotBounded(instructions="GRGL"))
print(isRobotBounded(instructions="GG"))