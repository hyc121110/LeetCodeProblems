# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def combinationSum2(candidates, target):
    res = []
    candidates.sort()
    dfs(candidates, target, 0, [], res)
    return res
    
def dfs(nums, target, index, path, res):
    if target < 0:
        return # backtracking
    if target == 0:
        res.append(path)
        return
    for i in range(index, len(nums)):
        if i > index and nums[i] == nums[i - 1]:
            continue
        if nums[i] > target:
            break

        dfs(nums, target - nums[i], i + 1, path + [nums[i]], res)

if __name__ == '__main__':
    candidates = [10,1,2,7,6,1,5]
    target = 8
    result = combinationSum2(candidates, target)
    print(result)                                                                                                                                                                          