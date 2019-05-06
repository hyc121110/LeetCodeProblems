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