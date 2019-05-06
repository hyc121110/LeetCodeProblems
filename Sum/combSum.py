'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

-All numbers (including target) will be positive integers.
-The solution set must not contain duplicate combinations.
'''

def combinationSum(candidates, target):
    def dfs(nums, target, index, path, res):
        if target < 0:
            # too large
            return # backtracking
        if target == 0:
            # found
            res.append(path)
            return
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            if nums[i] > target:
                break
            # reduce the target and extend the path as index
            # diff between comb2: i remains the same as we can
            # use the same repeated numbers
            dfs(nums, target - nums[i], i, path + [nums[i]], res)

    res = []
    candidates.sort()
    dfs(candidates, target, 0, [], res)
    return res

candidates=[2,3,6,7]
target=7
print(combinationSum(candidates,target))