'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
'''

'''
While iterating through all numbers, for each new number, we can either pick it or not pick it
1, if pick, just add current number to every existing subset.
2, if not pick, just leave all existing subsets as they are.
We just combine both into our result.
'''

def subset(nums):
    res = list()
    # base case with empty set
    res.append(list())

    for num in nums:
        size = len(res)
        for i in range(size):
            # add num to each of the subsets
            subset = list(res[i])
            subset.append(num)
            # added the subset to the result list
            res.append(subset)
    return res

print(subset(nums=[1,2,3]))