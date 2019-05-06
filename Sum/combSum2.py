'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
'''

def combinationSum2(candidates, target):
    candidates.sort()
    # use set to eliminate duplicate tuples
    dp = [set() for i in range(target+1)]
    dp[0].add(())
    for num in candidates:
        for t in range(target, num-1, -1):
            for prev in dp[t-num]:
                dp[t].add(prev + (num,))
    return list(dp[-1])

candidates = [10,1,2,7,6,1,5]
target = 8
print(combinationSum2(candidates,target))