'''
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
'''

def combinationSum4(candidates, target):
    # create array with size n + 1
    comb = [0] * (target + 1)
    comb[0] = 1
    
    #1st for loop: how many ways can get to i (target)
    for i in range(1,len(comb)):
        #2nd for loop: check elem in candidates can add to target
        for j in range(len(candidates)):
            if i - candidates[j] >= 0:
                comb[i] += comb[i - candidates[j]]
                
    return comb[target]

candidates = [1,2,3]
target = 6
print(combinationSum4(candidates, target))

# 1,1,1,1,1,1
# 1,1,1,1,2
# 1,1,1,3
# 1,1,2,2
# 1,2,3
# 2,2,2
# 3,3

#1: 1
#2: 1,1; 2
#3: 1,1,1; 1,2; 3
#4: 1,1,1,1; 1,1,2; 1,3; 2,2