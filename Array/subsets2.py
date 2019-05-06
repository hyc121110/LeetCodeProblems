'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
'''

def subsetsWithDup(nums):
    # similar to subset.py but with sorting and checking 
    # if subset in result list or not
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
            if subset not in res:
                res.append(subset)


print(subsetsWithDup(nums=[4,4,4,1,4]))