'''
You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.
'''

def reachNumber(target):
    target = abs(target)
    s = step = 0
    
    while s < target:
        step += 1
        s += step
    while ((s-target) % 2) != 0:
        step += 1
        s += step
    return step

print(reachNumber(target=8))