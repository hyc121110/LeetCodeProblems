'''
Given an array A of integers, return true if and only if we can partition the 
array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] 
+ A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + 
A[A.length - 1])
'''

def canThreePartsEqualSum(A):
    # idea: if the total sum of the array is not divisible by 3, it is
    # impossible to partition the array into three parts
    s = sum(A)
    if s % 3 != 0:
        return False
    # find the required sum
    s /= 3
    # array for matching sum
    targets = [2 * s, s]
    acc = 0
    for a in A:
        acc += a
        if acc == targets[-1]:
            targets.pop()
        if not targets:
            # all arrays have been partitioned
            return True
    return False

print(canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))